//
// Created by ziv on 30/04/17.
//

#ifndef TRYSCREEN_CONSTS_H
#define TRYSCREEN_CONSTS_H

#define FONT_WIDTH 6
#define FONT_HEIGHT 13
#define FONT_REGULAR u8g2_font_6x13_tf
#define FONT_BOLD u8g2_font_6x13B_tf

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

#define CHARACTERS_VISIBLE (SCREEN_WIDTH/FONT_WIDTH)
#define BUFFER_SIZE (CHARACTERS_VISIBLE + 1)

#endif //TRYSCREEN_CONSTS_H
