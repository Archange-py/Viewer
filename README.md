# Pictures Viewer
###

<p align="center" width="100%">
<img src=".\pictures\block.png" alt="block">
</p>

This project is an image editor currently in 16*16 format, recommended for Minecraft block and item textures. It runs on the Numworks calculator and on the computer, as long as the [required dependencies](https://github.com/Archange-py/Visuel) are installed (follow instructions in the Visuel repository). It is used by installing [viewer.py](viewer.py) and [examples_pictures.py](examples_pictures.py) alone on the calculator. To get the most out of it, follow the mini-tutorial in the [Tuto](#tuto) section.

You can install it directly on your calculator, by going to [my script](https://my.numworks.com/python/archange/viewer) and to [examples pictures](https://my.numworks.com/python/archange/examples_pictures) on the Numworks website.

## Table of Contents
***
1. [Tuto](#tuto)
2. [Keys Short](#keys-short)
3. [Settings](#settings)
4. [Examples](#examples)

## Tuto
***

I. First of all, to create a new image, go to "edit".


<p align="center" width="100%">
<img src=".\pictures\edit.png" alt="edit">
</p>

> If you've previously changed the default color, and your image doesn't have this color and remains white, press the "dot" key.

II. Then, use the [shortcuts](#keys-short) presented here to create your image, and then press "ans" to print the list containing the rgb values of your image in the console.

<p align="center" width="100%">
<img src=".\pictures\tuto_picture_1.png" alt="tuto_picture">
</p>

III. Then, copy and paste your code into the example file included with this project, by creating a new variable.

IIII. Finally, restart the viewer and observe your pre-loaded artwork by going to the "show" section !

<p align="center" width="100%">
<img src=".\pictures\tuto_picture_2.png" alt="tuto_picture">
</p>

## Keys Short
***

Here are all the keys you can use in the "Edit" section: 

<table>
    <thead>
        <th>Keys</th>
        <th>Short</th>
    </thead>
    <tbody>
        <tr>
            <td>Ok and Left Arrow</td>
            <td>Changes rgb channel counter-clockwise</td>
        </tr>
        <tr>
            <td>Ok and Right Arrow</td>
            <td>Changes rgb channel clockwise</td>
        </tr>
        <tr>
            <td>Up Arrow</td>
            <td>Moves cursor up</td>
        </tr>
        <tr>
            <td>Down Arrow</td>
            <td>Moves cursor Down</td>
        </tr>
        <tr>
            <td>Left Arrow</td>
            <td>Moves cursor Left</td>
        </tr>
        <tr>
            <td>Right Arrow</td>
            <td>Moves cursor Right</td>
        </tr>
        <tr>
            <td>Plus</td>
            <td>Increases the value of the pixel on which the cursor is located to the level of the selected rgb channel.</td>
        </tr>
        <tr>
            <td>Minus</td>
            <td>Decreases the value of the pixel on which the cursor is located to the level of the selected rgb channel.</td>
        </tr>
        <tr>
            <td>Ans</td>
            <td>Save the image for later viewing in "show", and print the image list line by line in the console.</td>
        </tr>
        <tr>
            <td>Dot</td>
            <td>Resets the image being edited to the default color.</td>
        </tr>
        <tr>
            <td>Exp</td>
            <td>Eraser - Erases the cursor box and replaces it with the default color.</td>
        </tr>
        <tr>
            <td>Backspace</td>
            <td>Exits "edit" mode while saving image modifications.</td>
        </tr>
    </tbody>
</table>

> Warning ! Key ANS is key "O", key DOT is key ":" and key EXP is key "5" on computer   

## Settings
***

This section presents the various possible parameters:

1. Pas: To increase the depth that is removed when you modify the value of a pixel's channel.

2. Size: NotImplemented

3. Time: To accelerate or decelerate the cursor speed.

4. To change the default color when a new image is created.

> Ignore the size parameter, as it is there for a future implementation.

## Examples
***

<table>
    <thead>
        <th align="center">Menu</th>
    </thead>
    <tbody>
        <td> <img src=".\pictures\menu.png"> </td>
    </tbody>
</table>

<table>
    <thead>
        <th align="center">Edit</th>
    </thead>
    <tbody>
        <td> <img src=".\pictures\edit.png"> </td>
    </tbody>
</table>

<table>
    <thead>
        <th align="center">Show</th>
        <th align="center">Show</th>
    </thead>
    <tbody>
        <td> <img src=".\pictures\show_cursor.png"> </td>
        <td> <img src=".\pictures\show_block.png"> </td>
    </tbody>
</table>

<table>
    <thead>
        <th align="center">Settings</th>
    </thead>
    <tbody>
        <td> <img src=".\pictures\settings.png"> </td>
    </tbody>
</table>
