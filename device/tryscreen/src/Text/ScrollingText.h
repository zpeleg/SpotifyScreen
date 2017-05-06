//
// Created by ziv on 24/04/17.
//

#ifndef TRYSCREEN_SCROLLINGTEXT_H
#define TRYSCREEN_SCROLLINGTEXT_H

#include "U8g2lib.h"
#include "ScrollingChar.h"
#include "Consts.h"
#include "BaseText.h"

class ScrollingText : public BaseText {
public:
    ScrollingText(U8G2 *screen, const char *text, int speed, u8g2_uint_t y);

    virtual ~ScrollingText();

    void Display(unsigned long currentMilliseconds);

private:
    U8G2 *screen;
    char *text;
    uint textLength;
    int moveDelay;
    u8g2_uint_t y;
    ScrollingChar characterBuffer[BUFFER_SIZE];
    int currentIndex;
    ulong lastMove;


    void InitScrollingChars();
};


#endif //TRYSCREEN_SCROLLINGTEXT_H
