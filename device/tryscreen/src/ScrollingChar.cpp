//
// Created by ziv on 29/04/17.
//

#include "ScrollingChar.h"
#include "Consts.h"

ScrollingChar::ScrollingChar(char character, u8g2_uint_t y, u8g2_uint_t initialX, U8G2 *screen) : y(y), x(initialX),
                                                                                                  screen(screen) {
    this->character[0] = character;
    this->character[1] = 0;
}

ScrollingChar::ScrollingChar() {
    y = 0;
    x = 0;
    screen = 0;
    character[0] = ' ';
    character[1] = NULL;
}

void ScrollingChar::Draw() {
    if (screen != 0) {
        screen->drawStr(x, y, character);
    }
}

void ScrollingChar::Move(u8g2_uint_t amount) {
    x -= amount;
}

bool ScrollingChar::ShouldDelete() {
    return x == (255 - FONT_WIDTH);
}

ScrollingChar::ScrollingChar(ScrollingChar &other) {
    this->x = other.x;
    this->y = other.y;
    this->screen = other.screen;
    this->character[0] = other.character[0];
    this->character[1] = other.character[1];
}

