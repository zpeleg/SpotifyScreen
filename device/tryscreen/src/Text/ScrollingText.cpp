//
// Created by ziv on 24/04/17.
//

#include "ScrollingText.h"
#include "Consts.h"

// Speed is px/s
ScrollingText::ScrollingText(U8G2 *screen, const char *text, int speed, u8g2_uint_t y) : screen(screen),
                                                                                         moveDelay(1000 / speed),
                                                                                         y(y) {

    this->text = new char[strlen(text) + 5];
    strcpy(this->text, text);
    strcat(this->text, "     ");
    textLength = strlen(this->text);
    currentIndex = 0;

    this->InitScrollingChars();
}

void ScrollingText::InitScrollingChars() {
    for (currentIndex = 0; currentIndex < BUFFER_SIZE; ++currentIndex) {
        characterBuffer[currentIndex % BUFFER_SIZE] = ScrollingChar(text[currentIndex % textLength], y,
                                                                    FONT_WIDTH * currentIndex,
                                                                    screen);
    }
}

void ScrollingText::Display(unsigned long currentMilliseconds) {
    if (currentMilliseconds - lastMove > moveDelay) {
        for (int i = 0; i < BUFFER_SIZE; ++i) {
            characterBuffer[i].Move(1);
        }
        lastMove = currentMilliseconds;
    }

    for (int i = 0; i < BUFFER_SIZE; ++i) {
        characterBuffer[i].Draw();
    }
    for (int i = 0; i < BUFFER_SIZE; ++i) {
        if (characterBuffer[i].ShouldDelete()) {
            characterBuffer[i] = ScrollingChar();
            characterBuffer[currentIndex % BUFFER_SIZE] = ScrollingChar(text[currentIndex % textLength], y,
                                                                        127,
                                                                        screen);
            currentIndex++;
        }
    }
}

ScrollingText::~ScrollingText() {

}
