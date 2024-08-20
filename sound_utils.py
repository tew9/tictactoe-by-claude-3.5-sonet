import pygame
import numpy as np

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

def create_tone(frequency, duration, volume=0.5):
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(2 * np.pi * frequency * t) * volume
    wave = np.repeat(wave.reshape(len(wave), 1), 2, axis=1)
    sound = pygame.sndarray.make_sound((wave * 32767).astype(np.int16))
    return sound

def test_sound():
    print("Testing sound...")
    tone = create_tone(440, 0.5)
    tone.play()
    pygame.time.wait(500)  # Wait for the sound to finish playing
    print("Sound test complete. Did you hear a beep?")

if __name__ == "__main__":
    pygame.init()
    test_sound()
    pygame.quit()