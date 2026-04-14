import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt

model = load_model("plant_model.h5")

img_path = "test.jpg"

img = image.load_img(img_path, target_size=(128, 128))
img_array = image.img_to_array(img)/255.0
img_array = np.expand_dims(img_array, axis=0)

prediction = model.predict(img_array)

print("Predicted class index:", np.argmax(prediction))
print("Confidence:", np.max(prediction))

plt.imshow(img)
plt.title("Prediction Result")
plt.axis('off')
plt.show()
