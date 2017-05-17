//
// Created by ziv on 06/05/17.
//

#ifndef TRYSCREEN_STATICTEXT_H
#define TRYSCREEN_STATICTEXT_H


#include <U8g2lib.h>
#include "BaseText.h"

class StaticText : public BaseText {
public:
    StaticText(U8G2 *screen, const char *text, u8g2_uint_t y);

    virtual ~StaticText() {}

    void Display(unsigned long currentMilliseconds);

private:
    const char *text;
    U8G2 *screen;
    u8g2_uint_t y;
};


#endif //TRYSCREEN_STATICTEXT_H
