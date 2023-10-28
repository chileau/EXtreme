# include <reg51.h> // Include the 8051 header file

unsigned char bcdToAscii(unsigned char bcdValue) {
    unsigned char tens, ones

    // Extract tens and ones digits from BCD
    tens = bcdValue >> 4
    ones = bcdValue & 0x0F

    // Convert BCD to ASCII representation
    if (tens <= 9) {
        tens += '0'
        // Convert to ASCII character
    }
    if (ones <= 9) {
        ones += '0'
        // Convert to ASCII character
    }

    return ((tens << 4) | ones)
    // Combine the ASCII digits
}

void main() {
    unsigned char bcdValue = 0x37
    // Example BCD value(from 37 BCD to ASCII)
    unsigned char asciiValue

    // Convert BCD to ASCII
    asciiValue = bcdToAscii(bcdValue)

    // Your main program logic here

    while (1) {
        // Main program loop
    }
}
