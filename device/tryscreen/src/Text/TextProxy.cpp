//
// Created by ziv on 06/05/17.
//

#include "TextProxy.h"
#include "Consts.h"
#include "ScrollingText.h"
#include "StaticText.h"

TextProxy::TextProxy(U8G2 *screen, const char *text, u8g2_int_t y) {
    if (strlen(text) > CHARACTERS_VISIBLE) {
        displayText = new ScrollingText(screen, text, TEXT_SPEED, y);
    } else {
        displayText = new StaticText(screen, text, y);
    }
}

void TextProxy::Display(unsigned long currentTime) {
    displayText->Display(currentTime);
}

TextProxy::~TextProxy() {
    delete displayText;
}
