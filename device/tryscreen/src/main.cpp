//
// Created by ziv on 08/04/17.
//

#include <ESP8266WiFi.h>
#include "Arduino.h"
#include "SPI.h"
#include "Wire.h"
#include "U8g2lib.h"
#include "ScrollingText.h"

//U8G2_SH1106_128X64_NONAME_F_4W_HW_SPI screen(U8G2_R0, /* cs=*/ 10, /* dc=*/ 9, /* reset=*/ 8);
U8G2_SH1106_128X64_NONAME_F_4W_HW_SPI *screen;//(U8G2_R0, 15, 5, 0);
ScrollingText *text;

void setup() {
    WiFi.forceSleepBegin();
    delay(1);
    Serial.begin(115200);
    screen = new U8G2_SH1106_128X64_NONAME_F_4W_HW_SPI(U8G2_R0, 15, 5, 0);
    screen->begin();
    text = new ScrollingText("This is a very long text, please don't crash my program", screen, 60, 20);
    //Wire.setClock(400000);
}

u8g2_uint_t x = 0;

// Three Movements from Petrushka: I. Russian Dance
// Modest Mussorgsky, Khatia Buniatishvili
// Kaleidoscope - Mussorgsky, Ravel, Stravinsky
String title = "Three Movements from Petrushka: I. Russian Dance";
String artists = "Modest Mussorgsky, Khatia Buniatishvili";
String album = "Kaleidoscope - Mussorgsky, Ravel, Stravinsky";
long lastMillis = 0;

void loop() {
    screen->clearBuffer();
    Serial.println("hi");
    screen->setFont(u8g2_font_8x13B_tf);
    text->Display(millis());
    Serial.println("bi");
    wdt_reset();
    screen->sendBuffer();
    delay(5);
}