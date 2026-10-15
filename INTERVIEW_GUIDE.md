# DeepVision AI — Interview Guide

## 30-second explanation

“DeepVision AI is a computer-vision project for classifying steel surface images into six defect categories. I trained a CNN in Google Colab using labeled images, evaluated it on a held-out test set, and exported the model. I then built a Streamlit app that loads the trained model and displays the predicted defect class and top-three confidence scores. It is a learning prototype, not a certified industrial inspection system.”

## Questions to practise

**1. What is deep learning?**  
A subset of machine learning that uses neural networks with multiple layers to learn useful representations from data.

**2. Why use a CNN for images?**  
Convolutional layers learn local patterns such as edges, textures, and shapes. Pooling reduces spatial dimensions and can make features less sensitive to small shifts.

**3. What is an epoch?**  
One complete pass through the training dataset.

**4. What is a batch?**  
A subset of training examples processed before the model updates its weights.

**5. What is overfitting?**  
When the model learns the training examples too closely and performs worse on unseen data. Compare training and validation curves; use augmentation, dropout, and early stopping where appropriate.

**6. What is the difference between training, validation, and test data?**  
Training updates model weights. Validation helps monitor/tune training. Test data is held back for a final evaluation after choices are made.

**7. What is categorical cross-entropy?**  
A loss function that penalizes the model when it assigns low probability to the correct class.

**8. What is backpropagation?**  
The process of calculating how much each model parameter contributed to the loss, so an optimizer can update the weights.

**9. Why do accuracy and F1-score both matter?**  
Accuracy is the fraction of all predictions that are correct. F1 balances precision and recall, which is useful when mistakes across classes have different patterns or class balance changes.

**10. Does confidence mean certainty?**  
No. It is the model’s output score. A high score can still be wrong, especially on images unlike the training data.

**11. Is this object detection?**  
No. This version classifies the whole image. Object detection/localization would require bounding-box labels and a different model/output design.

**12. What would you improve next?**  
Add Grad-CAM explanations, compare with transfer learning, perform robust testing on external images, track model versions, and integrate a human review step.

## Be honest about results

Do not memorize a made-up accuracy. Read the measured metrics printed by your own Colab run and describe the test split used. Mention limitations and example failure cases.
