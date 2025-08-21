#include "helpers.h"
#include "math.h"
#include "string.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop over all the pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Get rgb values
            int r = image[i][j].rgbtRed;
            int g = image[i][j].rgbtGreen;
            int b = image[i][j].rgbtBlue;

            // Calculate RGB value average for the pixel (as float) and round
            int avg = round((r + g + b) / 3.0);

            // Update the RGB values for the pixel to the average
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop over all the pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Get rgb values
            int r = image[i][j].rgbtRed;
            int g = image[i][j].rgbtGreen;
            int b = image[i][j].rgbtBlue;

            // Compute sepia values based on formula
            int sr = round(0.393 * r + 0.769 * g + 0.189 * b);
            int sg = round(0.349 * r + 0.686 * g + 0.168 * b);
            int sb = round(0.272 * r + 0.534 * g + 0.131 * b);

            // Update pixel RGB values to the sepia values
            // If values are over 255, set to 255 using fmin()
            image[i][j].rgbtRed = fmin(sr, 255);
            image[i][j].rgbtGreen = fmin(sg, 255);
            image[i][j].rgbtBlue = fmin(sb, 255);
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Create a temporary pixel for swaping values
    RGBTRIPLE temp_pixel;

    // Loop over all pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            // Swap pixels across the horizontal axis
            temp_pixel = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp_pixel;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Create a temporary image to copy original to
    RGBTRIPLE copy_image[height][width];

    // Copy the original image to the temp_image to use to get
    // RGB values from since we are changing the original image values
    memcpy(copy_image, image, sizeof(RGBTRIPLE) * height * width);

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float pixels = 0.0;

            int r = 0;
            int g = 0;
            int b = 0;

            // Loop over the 3x3 square around pixel (or 3x2 if boundary pixel)
            for (int k = -1; k <= 1; k++)
            {
                for (int l = -1; l <= 1; l++)
                {
                    // If current row + next row are within 3x3 square
                    // If current column + next column are within 3x3 square
                    if (i + k != height && i + k != -1 && j + l != width && j + l != -1)
                    {
                        // Update RGB values to the sum both pixels' RGB values
                        r += copy_image[i + k][j + l].rgbtRed;
                        g += copy_image[i + k][j + l].rgbtGreen;
                        b += copy_image[i + k][j + l].rgbtBlue;
                        // Increment pixels
                        pixels++;
                    }
                }
            }
            // Update RGB values to averaged/blurred values
            image[i][j].rgbtRed = round(r / pixels);
            image[i][j].rgbtGreen = round(g / pixels);
            image[i][j].rgbtBlue = round(b / pixels);
        }
    }
}
