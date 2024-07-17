#include "helpers.h"
#include <math.h>
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sum = 0;
            sum += image[i][j].rgbtRed;
            sum += image[i][j].rgbtGreen;
            sum += image[i][j].rgbtBlue;
            int result = roundf((float) sum / 3);
            image[i][j].rgbtRed = result;
            image[i][j].rgbtGreen = result;
            image[i][j].rgbtBlue = result;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            int helper_Red = image[i][j].rgbtRed;
            int helper_Green = image[i][j].rgbtGreen;
            int helper_Blue = image[i][j].rgbtBlue;
            image[i][j].rgbtRed = image[i][width - (j + 1)].rgbtRed;
            image[i][j].rgbtGreen = image[i][width - (j + 1)].rgbtGreen;
            image[i][j].rgbtBlue = image[i][width - (j + 1)].rgbtBlue;
            image[i][width - (j + 1)].rgbtRed = helper_Red;
            image[i][width - (j + 1)].rgbtGreen = helper_Green;
            image[i][width - (j + 1)].rgbtBlue = helper_Blue;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copied_image[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int Red_Sum = 0;
            int Green_Sum = 0;
            int Blue_Sum = 0;

            int counter = 0;

            for (int z = -1; z < 2; z++)
            {
                for (int x = -1; x < 2; x++)
                {
                    if (i + z < 0 ||
                        i + z > height - 1 ||
                        j + x < 0 ||
                        j + x > width - 1)
                    {
                        Red_Sum += 0;
                        Green_Sum += 0;
                        Blue_Sum += 0;
                    }
                    else
                    {
                        Red_Sum += image[i + z][j + x].rgbtRed;
                        Green_Sum += image[i + z][j + x].rgbtGreen;
                        Blue_Sum += image[i + z][j + x].rgbtBlue;
                        counter++;
                    }
                }
            }
            int Red = roundf((float) Red_Sum / counter);
            int Green = roundf((float) Green_Sum / counter);
            int Blue = roundf((float) Blue_Sum / counter);

            copied_image[i][j].rgbtRed = Red;
            copied_image[i][j].rgbtGreen = Green;
            copied_image[i][j].rgbtBlue = Blue;
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = copied_image[i][j];
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copied_image[height][width];
    int gx_list[] = {-1, 0, 1, -2, 0, 2, -1, 0, 1};
    int gy_list[] = {-1, -2, -1, 0, 0, 0, 1, 2, 1};
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int gx_Red = 0;
            int gx_Green = 0;
            int gx_Blue = 0;

            int gy_Red = 0;
            int gy_Green = 0;
            int gy_Blue = 0;

            int counter = 0;

            for (int z = -1; z < 2; z++)
            {
                for (int x = -1; x < 2; x++)
                {
                    if (i + z < 0 ||
                        i + z > height - 1 ||
                        j + x < 0 ||
                        j + x > width -1)
                    {
                        gx_Red += 0;
                        gx_Green += 0;
                        gx_Blue += 0;

                        gy_Red += 0;
                        gy_Green += 0;
                        gy_Blue += 0;

                        counter++;
                    }
                    else
                    {
                        gx_Red += (image[i + z][j + x].rgbtRed) * gx_list[counter];
                        gx_Green += (image[i + z][j + x].rgbtGreen) * gx_list[counter];
                        gx_Blue += (image[i + z][j + x].rgbtBlue) * gx_list[counter];

                        gy_Red += (image[i + z][j + x].rgbtRed) * gy_list[counter];
                        gy_Green += (image[i + z][j + x].rgbtGreen) * gy_list[counter];
                        gy_Blue += (image[i + z][j + x].rgbtBlue) * gy_list[counter];

                        counter++;
                    }
                }
            }
            int combined_xy_Red = roundf(sqrt(gx_Red * gx_Red + gy_Red * gy_Red));
            int combined_xy_Green = roundf(sqrt(gx_Green * gx_Green + gy_Green * gy_Green));
            int combined_xy_Blue = roundf(sqrt(gx_Blue * gx_Blue + gy_Blue * gy_Blue));

            if (combined_xy_Red > 255)
            {
                combined_xy_Red = 255;
            }

            if (combined_xy_Green > 255)
            {
                combined_xy_Green = 255;
            }

            if (combined_xy_Blue > 255)
            {
                combined_xy_Blue = 255;
            }

            copied_image[i][j].rgbtRed = combined_xy_Red;
            copied_image[i][j].rgbtGreen = combined_xy_Green;
            copied_image[i][j].rgbtBlue = combined_xy_Blue;
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = copied_image[i][j];
        }
    }
    return;
}
