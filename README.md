Hello there this is my third year project of engineering in which we have done preprosseing in image using various firtertaion method on it.
Images of historical documents often have characteristics, such as wrinkles, faint writing, stains, bleed-through ink, and other issues. 
These factors distort the text visibility and affect the performance of binarization. 
Preserving these document images aids future generations in learning about a variety of subjects. 
This article presents a new binarization approach for historic documents. This work uses bilateral and unsharp filtering, Otsu thresholding, histogram analysis, and k-means clustering for dark spot removal as part of a multi-step image enhancement process. 
Applying an intensity-based mask raises the quality of pixels above a set threshold. Furthermore, the method includes two additional refinements: a concluding sharpening phase and an enhancement of color contrast. The performance of proposed binarization approach 
is assessed using the Flesch Reading Ease Formula. The findings reveal that the algorithm achieved its highest readability score when applied to degraded documents, with an average readability score of 96.44. This suggests the algorithm's efficacy in enhancing the readability 
of noisy images, particularly in the context of degraded documents. 

Methodology

For improved historic document image binarization, a combination of filtering approaches, including bilateral filter, k-means clustering, Otsu thresholding, sharpening filter, and unsharp masking, is suggested in this methodology
![Screenshot 2024-05-21 222230](https://github.com/rutujnagrale/Text-Recognition-Performance-Evaluation-through-Image-Preprocessing-and-OCR-Analysis/assets/123777612/85412f03-4931-47e2-a73e-a1c8d377dcaf)


This is how the flow chart of the filter will go on

And this are the output after the perprossing
run all.py file (other file like allin,allin1,allin3,allin4 are same but some different parameters.

![Screenshot (149)](https://github.com/rutujnagrale/Text-Recognition-Performance-Evaluation-through-Image-Preprocessing-and-OCR-Analysis/assets/123777612/af656241-38c5-4664-a4e6-de5370afe1ca)

![Screensho![Screenshot (147)](https://github.com/rutujnagrale/Text-Recognition-Performance-Evaluation-through-Image-Preprocessing-and-OCR-Analysis/assets/123777612/a62aaa18-2f15-4bdd-99ca-709b9b414538)
t (148)](https://github.com/rutujnagrale/Text-Recognition-Performance-Evaluation-through-Image-Preprocessing-and-OCR-Analysis/assets/123777612/c0292215-cc6d-43d8-a75d-2f5bfd9b0f53)
![Screenshot (146)](https://github.com/rutujnagrale/Text-Recognition-Performance-Evaluation-through-Image-Preprocessing-and-OCR-Analysis/assets/123777612/ef5dc90e-0c81-4f55-b8d9-1add0a890fb0)
![Screenshot (145)](https://github.com/rutujnagrale/Text-Recognition-Performance-Evaluation-through-Image-Preprocessing-and-OCR-Analysis/assets/123777612/7d95b508-8991-4967-acf2-35aa7680f6bd)
![Screenshot (144)](https://github.com/rutujnagrale/Text-Recognition-Performance-Evaluation-through-Image-Preprocessing-and-OCR-Analysis/assets/123777612/370c1c07-b931-4377-8ae2-20ca74022623)
![Screenshot (143)](https://github.com/rutujnagrale/Text-Recognition-Performance-Evaluation-through-Image-Preprocessing-and-OCR-Analysis/assets/123777612/064208a4-2f77-44c4-8013-c7c80d03ddaf)
![Screenshot (142)](https://github.com/rutujnagrale/Text-Recognition-Performance-Evaluation-through-Image-Preprocessing-and-OCR-Analysis/assets/123777612/09aed952-d0d6-4561-bbd0-1d0363de884c)


To get a detail overview about this entire projecct you can refer to paper Report.txt in that each and every detail is given of this project

Happy coding !!!!
