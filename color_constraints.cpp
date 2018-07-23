bool imageProcessor::isHumanSkinRGB(int red, int green, int blue)
{

    float h, s, v;
    float Y, Cb, Cr;

    float fr = (float)red;
    float fg = (float)green;
    float fb = (float)blue;

    

    RGBToHSV(fr, fg, fb, h, s, v);
    RGBToYCbCr(red, green, blue, Y, Cb, Cr);

 

    syslog(LOG_DEBUG, "Conversion (%f,%f, %f) (%f,%f, %f) (%f,%f, %f)", red, green, blue, h, s, v, Y, Cb, Cr);
    //not filtering some yellows... (15 -> 25 in red-green)
    bool t11 = h <= 50 && h >= 0;
    bool t12 = s <= 0.68 && s > 0.1;
    bool t13 = (red > 95) && (green > 40) && (blue > 20) && (red > green) && (red > blue) && fabs(red - green) > 15;

    bool test1 = t11 && t12 && t13;

    bool t21 = (Cr > 135) && Cb > 85 && Y > 80;
    bool t22 = Cr <= (1.5862 * Cb) + 20;
    bool t23 = Cr >= (0.3448 * Cb) + 76.2069;
    bool t24 = Cr >= (-4.5652 * Cb) + 234.5652;
    bool t25 = Cr <= (-1.15 * Cb) + 301.75;
    bool t26 = Cr <= (-2.2857 * Cb) + 432.85;
    bool test2 = t13 && t21 && t22 && t23 && t24 && t25 && t26;

    

    syslog(LOG_DEBUG, "Color Space Results (%d,%d)", test1, test2);

    return test1 || test2;
}