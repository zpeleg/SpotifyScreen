//
// Created by ziv on 05/05/17.
//

#include "IconDisplay.h"
#include "IconsData.h"

#define ICON_WIDTH 16
#define ICON_HEIGHT 16
#define PADDING 3

#define ICONS_ORIGIN_X 72
#define ICONS_ORIGIN_Y 45

#define SHUFFLE_X ICONS_ORIGIN_X
#define REPEAT_X (ICONS_ORIGIN_X+PADDING+ICON_WIDTH)
#define PLAY_X (ICONS_ORIGIN_X+(PADDING+ICON_WIDTH)*2)

IconDisplay::IconDisplay(U8G2 *screen) : screen(screen), current(IconViewModel()) {
}

void IconDisplay::Draw() {
    if (current.play) {
        screen->drawTriangle(PLAY_X + 0, ICONS_ORIGIN_Y + 0, PLAY_X + 14, ICONS_ORIGIN_Y + 7, PLAY_X + 0,
                             ICONS_ORIGIN_Y + 14);
    } else {
        screen->drawXBM(PLAY_X, ICONS_ORIGIN_Y, ICON_WIDTH, ICON_HEIGHT, pause_bits);
    }
    if (current.repeat) {
        screen->drawXBM(REPEAT_X, ICONS_ORIGIN_Y, ICON_WIDTH, ICON_HEIGHT, repeat_bits);
    }
    if (current.shuffle) {
        screen->drawXBM(SHUFFLE_X, ICONS_ORIGIN_Y, ICON_WIDTH, ICON_HEIGHT, shuffle_bits);
    }
}

void IconDisplay::UpdateStatus(const IconViewModel &newVm) {
    newVm.PrintDebug();
    current = newVm;
    Serial.println("Replaced");
    current.PrintDebug();
}
