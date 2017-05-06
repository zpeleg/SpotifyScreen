//
// Created by ziv on 06/05/17.
//

#include "StaticText.h"

StaticText::StaticText(U8G2 *screen, const char *text, u8g2_uint_t y) : text(text), screen(screen), y(y) {
}

void StaticText::Display(unsigned long currentMilliseconds) {
    screen->drawStr(2, y, text);
}