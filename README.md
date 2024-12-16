[info] More files will be added once we finish beta testing at Columbia University Irving Medical Center, NY, USA.
# RV-Volume-Prediction

**Abstract**:
Quantitative evaluation of right ventricular (RV) volumes is of paramount importance in many cardiovascular conditions and is best performed by cardiovascular magnetic resonance imaging (CMR). However, CMR scanners are scarce, costly, and lack portability. Two-dimensional transthoracic echocardiography (2DE) allows for widely available, low cost and bedside evaluation of RV size and function. 2DE-based quantitative RV analysis is nevertheless restricted by the lack of accurate models of the complex RV shape. In this paper, we propose to calculate the RV end-diastolic (ED) and end-systolic (ES) volume by using an attention-based deep learning (DL) model on tabular data. Morphological measurements (areas) from eight standardized 2DE views are used as input to the regression model along with age, cardiac phase and gender information. The proposed architecture comprises a feature tokenizer module to transform all features (categorical and numerical) to embeddings, before applying a stack of Transformer layers. Our pipeline is trained and tested on 50 ED and 50 ES RV volumes (100 in total). The predicted volumes are compared to reference CMR values. Our method achieved impressive performance (R
=0.975) on this relatively small-scale dataset, while it outperformed other state-of-the-art methods. The RV function evaluation using tabular Transformers shows promise. This work questions the superiority of tree-based ensemble models over DL-based solutions for tabular data in the context of functional imaging of the heart. Our pipeline is also appealing as it may allow building multi-modal cardiovascular frameworks, where only one part of the data is tabular, and other parts include images and text data.

![face](https://github.com/tuanaqeelbohoran/RV-Volume-Prediction/assets/120468459/b010a7e6-8d6c-4e40-9e23-14ccfdb8ad90)

**The patent details are as below**

United States Patent and Trademark Office (USPTO)

Electronic Filing System ID: 48081004

Title of the Invention: Systems and methods for attention-based deep learning for right ventricular quantification using two-dimensional echocardiography
 
Application number: 63469990

Attorney Docket Number: 070050.6706

Receipt Date: 31st May 2023

### References

Below is a citation for one of our research papers:

```bibtex
@InProceedings{10.1007/978-3-031-35302-4_30,
author="Bohoran, Tuan A.
and Kampaktsis, Polydoros N.
and McLaughlin, Laura
and Leb, Jay
and Moustakidis, Serafeim
and McCann, Gerry P.
and Giannakidis, Archontis",
editor="Bernard, Olivier
and Clarysse, Patrick
and Duchateau, Nicolas
and Ohayon, Jacques
and Viallon, Magalie",
title="Right Ventricular Volume Prediction by Feature Tokenizer Transformer-Based Regression of 2D Echocardiography Small-Scale Tabular Data",
booktitle="Functional Imaging and Modeling of the Heart",
year="2023",
publisher="Springer Nature Switzerland",
address="Cham",
pages="292--300"}
