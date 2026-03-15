<?php
/**
 * Plugin Name: Social Share Buttons
 * Description: Adds small Facebook, X, Instagram, and LinkedIn share buttons to the top right of post titles.
 * Version: 1.0.0
 * Author: Your Name
 * License: GPL2
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Enqueue plugin styles.
 */
function ssb_enqueue_styles() {
    wp_enqueue_style(
        'ssb-styles',
        plugin_dir_url( __FILE__ ) . 'social-share-buttons.css',
        [],
        '1.0.0'
    );
}
add_action( 'wp_enqueue_scripts', 'ssb_enqueue_styles' );

/**
 * Inject share buttons before post content on single posts.
 *
 * Note: Instagram does not support direct web share URLs like other platforms.
 * The Instagram button opens instagram.com so users can manually share.
 */
function ssb_add_share_buttons( $content ) {
    if ( ! is_single() || ! in_the_loop() || ! is_main_query() ) {
        return $content;
    }

    $post_url   = rawurlencode( get_permalink() );
    $post_title = rawurlencode( get_the_title() );

    $facebook_url  = 'https://www.facebook.com/sharer/sharer.php?u=' . $post_url;
    $x_url         = 'https://x.com/intent/tweet?url=' . $post_url . '&text=' . $post_title;
    $instagram_url = 'https://www.instagram.com/';
    $linkedin_url  = 'https://www.linkedin.com/sharing/share-offsite/?url=' . $post_url;

    $buttons = '<div class="ssb-share-buttons">';
    $buttons .= ssb_button( $facebook_url,  'Facebook',  'ssb-facebook',  ssb_icon_facebook() );
    $buttons .= ssb_button( $x_url,         'X',         'ssb-x',         ssb_icon_x() );
    $buttons .= ssb_button( $instagram_url, 'Instagram', 'ssb-instagram', ssb_icon_instagram() );
    $buttons .= ssb_button( $linkedin_url,  'LinkedIn',  'ssb-linkedin',  ssb_icon_linkedin() );
    $buttons .= '</div>';

    return $buttons . $content;
}
add_filter( 'the_content', 'ssb_add_share_buttons' );

/**
 * Render a single share button link.
 */
function ssb_button( $url, $label, $class, $icon_svg ) {
    return sprintf(
        '<a href="%s" class="ssb-btn %s" target="_blank" rel="noopener noreferrer" aria-label="Share on %s" title="Share on %s">%s</a>',
        esc_url( $url ),
        esc_attr( $class ),
        esc_attr( $label ),
        esc_attr( $label ),
        $icon_svg
    );
}

/** Facebook icon SVG */
function ssb_icon_facebook() {
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>';
}

/** X (Twitter) icon SVG */
function ssb_icon_x() {
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>';
}

/** Instagram icon SVG */
function ssb_icon_instagram() {
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z" fill="none" stroke-width="2"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5" stroke-width="2"/></svg>';
}

/** LinkedIn icon SVG */
function ssb_icon_linkedin() {
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>';
}
