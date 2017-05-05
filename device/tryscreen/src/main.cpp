//
// Created by ziv on 08/04/17.
//

#include <ESP8266WiFi.h>
#include "Arduino.h"
#include "SPI.h"
#include "Wire.h"
#include "U8g2lib.h"
#include "ScrollingText.h"
#include "Icons.h"

//U8G2_SH1106_128X64_NONAME_F_4W_HW_SPI screen(U8G2_R0, /* cs=*/ 10, /* dc=*/ 9, /* reset=*/ 8);
U8G2_SH1106_128X64_NONAME_F_4W_HW_SPI *screen;//(U8G2_R0, 15, 5, 0);
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
}

void loop() {
    screen->clearBuffer();
    screen->setFont(FONT_REGULAR);
    unsigned long currentTime = millis();
    text->Display(currentTime);
    text2->Display(currentTime);
    screen->setFont(FONT_BOLD);
    text1->Display(currentTime);

    screen->drawXBM(10, 64 - 20, 16, 16, shuffle_bits);
    screen->drawXBM(10 + 17, 64 - 20, 16, 16, repeat_bits);
    screen->drawXBM(10 + 17 * 2, 64 - 20, 16, 16, play_bits);
    screen->drawXBM(10 + 17 * 3, 64 - 20, 16, 16, pause_bits);

    int traX = 10 + 17 * 4;
    int traY = 64-20;
    screen->drawTriangle(traX + 0, traY + 0, traX + 14, traY + 7, traX + 0, traY + 14);
    screen->sendBuffer();
    yield();
}