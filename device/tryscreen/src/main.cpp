//
// Created by ziv on 08/04/17.
//

#include <ESP8266WiFi.h>
#include "Arduino.h"
#include "SPI.h"
#include "Wire.h"
#include "U8g2lib.h"
#include "ScrollingText.h"
#include "IconsData.h"
#include "IconDisplay.h"

//U8G2_SH1106_128X64_NONAME_F_4W_HW_SPI screen(U8G2_R0, /* cs=*/ 10, /* dc=*/ 9, /* reset=*/ 8);
U8G2_SH1106_128X64_NONAME_F_4W_HW_SPI *screen;//(U8G2_R0, 15, 5, 0);
IconDisplay *icons;
ScrollingText *text;
ScrollingText *text1;
ScrollingText *text2;

String title = "Three Movements from Petrushka: I. Russian Dance";
String artists = "Modest Mussorgsky, Khatia Buniatishvili";
String album = "Kaleidoscope - Mussorgsky, Ravel, Stravinsky";
#define SPEED 25

void setup() {
    WiFi.forceSleepBegin();
    delay(1);
    Serial.begin(115200);
    screen = new U8G2_SH1106_128X64_NONAME_F_4W_HW_SPI(U8G2_R0, 15, 5, 0);
    screen->begin();
    text = new ScrollingText(title.c_str(), screen, SPEED, FONT_HEIGHT);
    text1 = new ScrollingText(artists.c_str(), screen, SPEED, FONT_HEIGHT * 2);
    text2 = new ScrollingText(album.c_str(), screen, SPEED, FONT_HEIGHT * 3);
    icons = new IconDisplay(screen);
    const IconViewModel model(true, true, true);
    model.PrintDebug();
    icons->UpdateStatus(model);
}

int counter = 0;
unsigned long lastTime = 0;
unsigned long delayTime = 1000;

void loop() {
    screen->clearBuffer();

    unsigned long currentTime = millis();

    screen->setFont(FONT_REGULAR);
    text->Display(currentTime);
    text2->Display(currentTime);
    screen->setFont(FONT_BOLD);
    text1->Display(currentTime);

    icons->Draw();

    screen->sendBuffer();
    if (currentTime - lastTime > delayTime) {
        lastTime = currentTime;
        IconViewModel model(counter & 0x1, counter & 0x2, counter & 0x4);
        icons->UpdateStatus(model);
        counter++;
    }
}