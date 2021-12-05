from sense_hat import SenseHat
import time

sense = SenseHat();

V = [57, 255, 20];
A = [255, 255, 0];
N = [255, 112, 40];
R = [255, 0, 0];
O = [0, 0, 0];

sense.set_rotation(180);

'''
prueba_colores = [
        V, V, V, V, V, V, V, V,
        V, V, V, V, V, V, V, V,
        A, A, A, A, A, A, A, A,
        A, A, A, A, A, A, A, A,
        N, N, N, N, N, N, N, N,
        N, N, N, N, N, N, N, N,
        R, R, R, R, R, R, R, R,
        R, R, R, R, R, R, R, R
        ];

sense.set_pixels(prueba_colores);
'''

sense.show_message("Hello world"); 

'''
POSICIONES INCLINÓMETRO

3, 3, 3, 3, 3, 3, 3, 3, 
3, 2, 2, 2, 2, 2, 2, 3, 
3, 2, 1, 1, 1, 1, 2, 3, 
3, 2, 1, 0, 0, 1, 2, 3,
3, 2, 1, 0, 0, 1, 2, 3, 
3, 2, 1, 1, 1, 1, 2, 3, 
3, 2, 2, 2, 2, 2, 2, 3,
3, 3, 3, 3, 3, 3, 3, 3,
'''

led_incl_00 = [
        R, R, O, O, O, O, O, O,
        R, R, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_10 = [
        O, R, R, O, O, O, O, O,
        O, R, R, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O, 
        O, O, O, O, O, O, O, O
        ];

led_incl_20 = [
        O, O, R, R, O, O, O, O,
        O, O, R, R, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_30 = [
        O, O, O, R, R, O, O, O,
        O, O, O, R, R, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O 
        ];

led_incl_40 = [
        O, O, O, O, R, R, O, O,
        O, O, O, O, R, R, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_50 = [
        O, O, O, O, O, R, R, O,
        O, O, O, O, O, R, R, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_60 = [
        O, O, O, O, O, O, R, R,
        O, O, O, O, O, O, R, R,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_01 = [
        O, O, O, O, O, O, O, O,
        R, R, O, O, O, O, O, O,
        R, R, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_11 = [
        O, O, O, O, O, O, O, O,
        O, N, N, O, O, O, O, O,
        O, N, N, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_21 = [
        O, O, O, O, O, O, O, O,
        O, O, N, N, O, O, O, O,
        O, O, N, N, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_31 = [
        O, O, O, O, O, O, O, O,
        O, O, O, N, N, O, O, O,
        O, O, O, N, N, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_41 = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, N, N, O, O,
        O, O, O, O, N, N, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_51 = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, N, N, O,
        O, O, O, O, O, N, N, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_61 = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, R, R,
        O, O, O, O, O, O, R, R,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_02 = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        R, R, O, O, O, O, O, O,
        R, R, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_12 = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, N, N, O, O, O, O, O,
        O, N, N, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_22 = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, A, A, O, O, O, O,
        O, O, A, A, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_32 = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, A, A, O, O, O,
        O, O, O, A, A, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_42 = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, A, A, O, O,
        O, O, O, O, A, A, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_52 = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, N, N, O,
        O, O, O, O, O, N, N, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_62 = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, R, R,
        O, O, O, O, O, O, R, R,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_03 = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        R, R, O, O, O, O, O, O,
        R, R, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_13 = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, N, N, O, O, O, O, O,
        O, N, N, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_23 = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, A, A, O, O, O, O,
        O, O, A, A, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_33 = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, V, V, O, O, O,
        O, O, O, V, V, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_43 = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, A, A, O, O,
        O, O, O, O, A, A, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_53 = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, N, N, O,
        O, O, O, O, O, N, N, O, 
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

led_incl_63 = [
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, R, R,
        O, O, O, O, O, O, R, R,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O,
        O, O, O, O, O, O, O, O
        ];

sense.set_pixels(led_incl_00);
time.sleep(0.25);
sense.set_pixels(led_incl_10);
time.sleep(0.25);
sense.set_pixels(led_incl_20);
time.sleep(0.25);
sense.set_pixels(led_incl_30);
time.sleep(0.25);
sense.set_pixels(led_incl_40);
time.sleep(0.25);
sense.set_pixels(led_incl_50);
time.sleep(0.25);
sense.set_pixels(led_incl_60);
time.sleep(0.25);
sense.set_pixels(led_incl_01);
time.sleep(0.25);
sense.set_pixels(led_incl_11);
time.sleep(0.25);
sense.set_pixels(led_incl_21);
time.sleep(0.25);
sense.set_pixels(led_incl_31);
time.sleep(0.25);
sense.set_pixels(led_incl_41);
time.sleep(0.25);
sense.set_pixels(led_incl_51);
time.sleep(0.25);
sense.set_pixels(led_incl_61);
time.sleep(0.25);
sense.set_pixels(led_incl_02);
time.sleep(0.25);
sense.set_pixels(led_incl_12);
time.sleep(0.25);
sense.set_pixels(led_incl_22);
time.sleep(0.25);
sense.set_pixels(led_incl_32);
time.sleep(0.25);
sense.set_pixels(led_incl_42);
time.sleep(0.25);
sense.set_pixels(led_incl_52);
time.sleep(0.25);
sense.set_pixels(led_incl_62);
time.sleep(0.25);
sense.set_pixels(led_incl_03);
time.sleep(0.25);
sense.set_pixels(led_incl_13);
time.sleep(0.25);
sense.set_pixels(led_incl_23);
time.sleep(0.25);
sense.set_pixels(led_incl_33);
time.sleep(0.25);
sense.set_pixels(led_incl_43);
time.sleep(0.25);
sense.set_pixels(led_incl_53);
time.sleep(0.25);
sense.set_pixels(led_incl_63);
time.sleep(0.25);
