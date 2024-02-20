#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int rgbAvg = round(((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0));
            image[i][j].rgbtRed = rgbAvg;
            image[i][j].rgbtGreen = rgbAvg;
            image[i][j].rgbtBlue = rgbAvg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            float sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            float sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            else
            {
                image[i][j].rgbtRed = sepiaRed;
                image[i][j].rgbtGreen = sepiaGreen;
                image[i][j].rgbtBlue = sepiaBlue;
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        int rowWidth = width - 1;
        RGBTRIPLE tempArray[width];

        for (int j = 0; j < width; j++)
        {
            tempArray[j] = image[i][rowWidth--];
        }
        for (int k = 0; k < width; k++)
        {
            image[i][k] = tempArray[k];
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }
    for (int k = 0; k < height; k++)
    {
        for (int l = 0; l < width; l++)
        {
            float redSum = 0;
            float greenSum = 0;
            float blueSum = 0;
            int count = 0;
            if (k - 1 >= 0 && l - 1 >= 0)
            {
                redSum += copy[k - 1][l - 1].rgbtRed;
                greenSum += copy[k - 1][l - 1].rgbtGreen;
                blueSum += copy[k - 1][l - 1].rgbtBlue;
                count++;
            }
            if (k - 1 >= 0 && l >= 0)
            {
                redSum += copy[k - 1][l].rgbtRed;
                greenSum += copy[k - 1][l].rgbtGreen;
                blueSum += copy[k - 1][l].rgbtBlue;
                count++;
            }
            if (k - 1 >= 0 && l + 1 < width)
            {
                redSum += copy[k - 1][l + 1].rgbtRed;
                greenSum += copy[k - 1][l + 1].rgbtGreen;
                blueSum += copy[k - 1][l + 1].rgbtBlue;
                count++;
            }
            if (k >= 0 && l - 1 >= 0)
            {
                redSum += copy[k][l - 1].rgbtRed;
                greenSum += copy[k][l - 1].rgbtGreen;
                blueSum += copy[k][l - 1].rgbtBlue;
                count++;
            }
            if (k >= 0 && l + 1 < width)
            {
                redSum += copy[k][l + 1].rgbtRed;
                greenSum += copy[k][l + 1].rgbtGreen;
                blueSum += copy[k][l + 1].rgbtBlue;
                count++;
            }
            if (k >= 0 && l >= 0)
            {
                redSum += copy[k][l].rgbtRed;
                greenSum += copy[k][l].rgbtGreen;
                blueSum += copy[k][l].rgbtBlue;
                count++;
            }
            if (k + 1 < height && l - 1 >= 0)
            {
                redSum += copy[k + 1][l - 1].rgbtRed;
                greenSum += copy[k + 1][l - 1].rgbtGreen;
                blueSum += copy[k + 1][l - 1].rgbtBlue;
                count++;
            }
            if (k + 1 < height && l + 1 < width)
            {
                redSum += copy[k + 1][l + 1].rgbtRed;
                greenSum += copy[k + 1][l + 1].rgbtGreen;
                blueSum += copy[k + 1][l + 1].rgbtBlue;
                count++;
            }
            if (k + 1 < height && l >= 0)
            {
                redSum += copy[k + 1][l].rgbtRed;
                greenSum += copy[k + 1][l].rgbtGreen;
                blueSum += copy[k + 1][l].rgbtBlue;
                count++;
            }
            image[k][l].rgbtRed = round(redSum / count);
            image[k][l].rgbtGreen = round(greenSum / count);
            image[k][l].rgbtBlue = round(blueSum / count);
        }
    }
    return;
}
