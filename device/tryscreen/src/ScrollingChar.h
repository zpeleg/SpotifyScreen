//
// Created by ziv on 29/04/17.
//

#ifndef TRYSCREEN_SCROLLINGCHAR_H
#define TRYSCREEN_SCROLLINGCHAR_H


#include <clib/u8g2.h>
#include <U8g2lib.h>

class ScrollingChar {
public:
    ScrollingChar();
    ScrollingChar(ScrollingChar&);
    ScrollingChar(char character, u8g2_uint_t y, u8g2_uint_t initialX, U8G2 *screen);

    void Draw();

    void Move(u8g2_uint_t amount);

    bool ShouldDelete();

private:
    char character[2];
    u8g2_uint_t y;
    u8g2_uint_t x;
    U8G2 *screen;
};


#endif //TRYSCREEN_SCROLLINGCHAR_H
