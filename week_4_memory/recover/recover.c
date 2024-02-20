#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("usage ./recover filename\n");
        return 1;
    }

    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    uint8_t buffer[512];
    int fileCount = -1;
    char buffOut[50];
    FILE *output = NULL;
    while (fread(buffer, 1, 512, card) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (output != NULL)
            {
                fclose(output);
            }
            fileCount++;
            sprintf(buffOut, "%03i.jpg", fileCount);
            output = fopen(buffOut, "wb");
        }
        if (output != NULL)
        {
            fwrite(buffer, sizeof(uint8_t), 512, output);
        }
    }
    if (output != NULL)
    {
        fclose(output);
    }
    fclose(card);

    return 0;
}
