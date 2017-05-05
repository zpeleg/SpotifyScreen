//
// Created by ziv on 02/05/17.
//

#ifndef TRYSCREEN_ICONS_H
#define TRYSCREEN_ICONS_H

#define pause_width 16
#define pause_height 16
static unsigned char pause_bits[] = {
        0x00, 0x00, 0x00, 0x00, 0x78, 0x1e, 0x78, 0x1e, 0x78, 0x1e, 0x78, 0x1e,
        0x78, 0x1e, 0x78, 0x1e, 0x78, 0x1e, 0x78, 0x1e, 0x78, 0x1e, 0x78, 0x1e,
        0x78, 0x1e, 0x78, 0x1e, 0x00, 0x00, 0x00, 0x00 };
#define play_width 16
#define play_height 16
static unsigned char play_bits[] = {
        0x02, 0x00, 0x0e, 0x00, 0x3e, 0x00, 0xfe, 0x00, 0xfe, 0x03, 0xfe, 0x0f,
        0xfe, 0x3f, 0xfe, 0x7f, 0xfe, 0x3f, 0xfe, 0x0f, 0xfe, 0x03, 0xfe, 0x00,
        0x3e, 0x00, 0x0e, 0x00, 0x02, 0x00, 0x00, 0x00 };
#define repeat_width 16
#define repeat_height 16
static unsigned char repeat_bits[] = {
        0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00, 0x0c, 0xfc, 0x1f, 0x02, 0x4c,
        0x01, 0x84, 0x01, 0x80, 0x21, 0x80, 0x32, 0x40, 0xf8, 0x3f, 0x30, 0x00,
        0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };
#define shuffle_width 16
#define shuffle_height 16
static unsigned char shuffle_bits[] = {
        0x00, 0x00, 0x00, 0x20, 0x00, 0x40, 0x03, 0xf0, 0x0c, 0x4c, 0x10, 0x22,
        0x20, 0x01, 0xc0, 0x00, 0xc0, 0x00, 0x20, 0x01, 0x10, 0x22, 0x0c, 0x4c,
        0x03, 0xf0, 0x00, 0x40, 0x00, 0x20, 0x00, 0x00 };

#endif //TRYSCREEN_ICONS_H
