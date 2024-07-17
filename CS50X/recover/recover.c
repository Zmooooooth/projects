#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Invalid Usage: ./recover <filename>.raw\n");
        return 1;
    }
    char *inputfile = argv[1];
    FILE *in = fopen(inputfile, "r");
    if (in == NULL)
    {
        printf("Could not open %s!\n", inputfile);
        return 2;
    }
    uint8_t buffer[512];
    int image_counter = 0;
    FILE *out = NULL;
    while (fread(buffer, sizeof(uint8_t), 512, in) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && buffer[3] <= 0xef &&
            buffer[3] >= 0xe0)
        {
            if (out != NULL)
            {
                fclose(out);
                image_counter++;
            }
            char buff[8];
            sprintf(buff, "%03i.jpg", image_counter);
            out = fopen(buff, "w");
            if (out == NULL)
            {
                printf("Could not open file.\n");
                return 3;
            }
        }
        if (out != NULL)
        {
            fwrite(buffer, sizeof(uint8_t), 512, out);
        }
    }
    if (out != NULL)
    {
        fclose(out);
    }
    fclose(in);
    return 0;
}
