#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// size of the block that will be read and written
const int BLOCK_SIZE = 512;

int main(int argc, char *argv[])
{
    // Error if no argument
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover card.raw\n");
        return 1;
    }

    // Create infile as file name
    char *infile = argv[1];

    // Open the memory card read-only
    FILE *card = fopen(infile, "r");

    // Check if the file opened correctly
    if (card == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // Create a unsigned int buffer for a block of data
    uint8_t buffer[BLOCK_SIZE];

    // Create image for jpg file name
    char image[8];

    // # of images
    int image_count = 0;

    // Create a file pointer for output JPEGs
    FILE *outptr = NULL;

    // While there is still data left to read on the card
    while (fread(buffer, 1, BLOCK_SIZE, card) == BLOCK_SIZE)
    {
        // Look for beginning of jpg
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && buffer[3] >= 0xe0 &&
            buffer[3] <= 0xef)
        {
            // Close input files that are open
            if (image_count > 0)
            {
                fclose(outptr);
            }

            // Create a new image name
            sprintf(image, "%03d.jpg", image_count);

            // Open the new image file
            outptr = fopen(image, "w");

            // Check to see if new image file has been created
            if (outptr == NULL)
            {
                fprintf(stderr, "Could not create %s.\n", image);
                return 3;
            }

            // Increment # of image files
            image_count++;
        }

        // Create  JPEGs from the data if image file is open
        if (outptr != NULL)
        {
            // Write to JPEG file
            fwrite(buffer, BLOCK_SIZE, 1, outptr);
        }
    }
    // Close the image file
    fclose(outptr);

    // Close the card file
    fclose(card);

    return 0;
}
