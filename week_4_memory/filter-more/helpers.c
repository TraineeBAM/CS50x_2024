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

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
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
            float redSumGx = 0;
            float redSumGy = 0;
            float greenSumGx = 0;
            float greenSumGy = 0;
            float blueSumGx = 0;
            float blueSumGy = 0;

            if (k - 1 >= 0 && l - 1 >= 0)
            {
                redSumGx += (copy[k - 1][l - 1].rgbtRed * -1);
                greenSumGx += (copy[k - 1][l - 1].rgbtGreen * -1);
                blueSumGx += (copy[k - 1][l - 1].rgbtBlue * -1);
                redSumGy += (copy[k - 1][l - 1].rgbtRed * -1);
                greenSumGy += (copy[k - 1][l - 1].rgbtGreen * -1);
                blueSumGy += (copy[k - 1][l - 1].rgbtBlue * -1);
            }
            if (k - 1 >= 0 && l >= 0)
            {
                redSumGy += (copy[k - 1][l].rgbtRed * -2);
                greenSumGy += (copy[k - 1][l].rgbtGreen * -2);
                blueSumGy += (copy[k - 1][l].rgbtBlue * -2);
            }
            if (k - 1 >= 0 && l + 1 < width)
            {
                redSumGx += (copy[k - 1][l + 1].rgbtRed);
                greenSumGx += (copy[k - 1][l + 1].rgbtGreen);
                blueSumGx += (copy[k - 1][l + 1].rgbtBlue);
                redSumGy += (copy[k - 1][l + 1].rgbtRed * -1);
                greenSumGy += (copy[k - 1][l + 1].rgbtGreen * -1);
                blueSumGy += (copy[k - 1][l + 1].rgbtBlue * -1);
            }
            if (k >= 0 && l - 1 >= 0)
            {
                redSumGx += (copy[k][l - 1].rgbtRed * -2);
                greenSumGx += (copy[k][l - 1].rgbtGreen * -2);
                blueSumGx += (copy[k][l - 1].rgbtBlue * -2);
            }
            if (k >= 0 && l + 1 < width)
            {
                redSumGx += (copy[k][l + 1].rgbtRed * 2);
                greenSumGx += (copy[k][l + 1].rgbtGreen * 2);
                blueSumGx += (copy[k][l + 1].rgbtBlue * 2);
            }
            if (k + 1 < height && l - 1 >= 0)
            {
                redSumGx += (copy[k + 1][l - 1].rgbtRed * -1);
                greenSumGx += (copy[k + 1][l - 1].rgbtGreen * -1);
                blueSumGx += (copy[k + 1][l - 1].rgbtBlue * -1);
                redSumGy += (copy[k + 1][l - 1].rgbtRed);
                greenSumGy += (copy[k + 1][l - 1].rgbtGreen);
                blueSumGy += (copy[k + 1][l - 1].rgbtBlue);
            }
            if (k + 1 < height && l >= 0)
            {
                redSumGy += (copy[k + 1][l].rgbtRed * 2);
                greenSumGy += (copy[k + 1][l].rgbtGreen * 2);
                blueSumGy += (copy[k + 1][l].rgbtBlue * 2);
            }
            if (k + 1 < height && l + 1 < width)
            {
                redSumGx += (copy[k + 1][l + 1].rgbtRed);
                greenSumGx += (copy[k + 1][l + 1].rgbtGreen);
                blueSumGx += (copy[k + 1][l + 1].rgbtBlue);
                redSumGy += (copy[k + 1][l + 1].rgbtRed);
                greenSumGy += (copy[k + 1][l + 1].rgbtGreen);
                blueSumGy += (copy[k + 1][l + 1].rgbtBlue);
            }

            redSumGx = redSumGx * redSumGx;
            redSumGy = redSumGy * redSumGy;
            redSum = round(sqrt(redSumGx + redSumGy));
            if (redSum > 255)
            {
                redSum = 255;
            }
            greenSumGx = greenSumGx * greenSumGx;
            greenSumGy = greenSumGy * greenSumGy;
            greenSum = round(sqrt(greenSumGx + greenSumGy));
            if (greenSum > 255)
            {
                greenSum = 255;
            }
            blueSumGx = blueSumGx * blueSumGx;
            blueSumGy = blueSumGy * blueSumGy;
            blueSum = round(sqrt(blueSumGx + blueSumGy));
            if (blueSum > 255)
            {
                blueSum = 255;
            }
            image[k][l].rgbtRed = redSum;
            image[k][l].rgbtGreen = greenSum;
            image[k][l].rgbtBlue = blueSum;
        }
    }
    return;
}

// (76 117 255)  (213 228 255) (192 190 255)
// (114 102 255) (210 150 60)  (103 108 255)
// (114 117 255) (200 197 255) (210 190 255)

// (76 117 255)  (213 228 255) (212 201 255)
// (114 102 255) (210 150 60)  (42 76 247)
// (114 117 255) (200 197 255) (221 204 255)
