//
// Created by ziv on 06/05/17.
//

#ifndef TRYSCREEN_TEXTPROXY_H
#define TRYSCREEN_TEXTPROXY_H

#include <U8g2lib.h>
#include "BaseText.h"


class TextProxy {
public:
    TextProxy(U8G2 *screen, const char *text, u8g2_int_t y);
    virtual ~TextProxy();

    void Display(unsigned long currentTime);

private:
    BaseText *displayText;
};


#endif //TRYSCREEN_TEXTPROXY_H
