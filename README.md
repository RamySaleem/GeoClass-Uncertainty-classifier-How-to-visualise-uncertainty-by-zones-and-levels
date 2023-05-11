# GeoClass--Uncertainty-classifier-How-to-visualise-uncertainty-by-zones-and-levels?
This model is a simple method to classify, quantify and illustrate the uncertainty in subsurface interpretation using python open source libraries. This model takes a practical and coding focused approach to visualise the uncertainty in subsurface interpretations by calculating zones and levels of uncertainty—the Five uncertainty zones created by measuring the distance from outcrops, galleries and boreholes.

# Read our Poster 
![](https://i.imgur.com/mEXMs7L.jpg)
# Abstract

  Subsurface geological structures are generally complicated and very hard to interpret. This algorithm aims to use Python coding language to visualise and measure the uncertainty in subsurface geological interpretations of any subsurface structure from sparse and incomplete datasets. The complex history of geological structures is difficult to unravel from limited data, and ‘accurate’ interpretations are associated with subsurface structural interpretation uncertainties. These challenges often result in the employment of heuristics, rules of thumb, and know solutions to subsurface interpretations that introduced bias. Excellent visualisation provided by Open 3D as a modern open-source library created for massive data processing makes such library perfect for visualising interpretations of subsurface structural geometries. However, illustrating and quantifying uncertainty in geological interpretations of subsurface cross-sections is still ambiguous. Here we provide an automatic data-driven approach model to illustrate and quantify uncertainty using subsurface cross-sections of geological/structural geometries. Five zones have been calculated to display uncertainty in geological cross-section interpretations. These five uncertainty zones are applied to horizons and faults interpretations. Together they form a critical part of the dataset. These calculated uncertainty zones and levels allow the investigation of cross-section building and interpretation from level 1, where direct observations of the rock can be made, outwards, whilst illustrating increasing uncertainty. Our uncertainty classification model applies to any sub-surface datasets and can be used to inform approaches to sub-surface interpretations elsewhere. We claim that quantifying uncertainty by zones and levels can provide a framework for reducing interpretation risk and improving the visualisation of uncertainties in subsurface cross-sections.

# Overview
  This model is a simple method to classify, quantify and illustrate the uncertainty in subsurface interpretation using python open source libraries. This model takes a practical and coding focused approach to visualise the uncertainty in subsurface interpretations by calculating zones and levels of uncertainty—the Five uncertainty zones created by measuring the distance from outcrops, galleries and boreholes.

![](https://i.imgur.com/WyH9BS5.png)

Schematic model to illustrate uncertainty and risk zones and associated uncertainty nomenclature for horizons and faults interpretations. (a) Uncertainty zones defined by five levels. Zone-1 it is the most certain zone and defines as the area of the outcrops and galleries. Zone-2 it is the certain zone and defines as the areas around outcrops and between galleries. Zone-3 it is the possible zone and defines as the area within 100m from the data source. Zone-4 it is the uncertain zone and defines as the area beyond 100m from the data source. Zone-5 it is the least certain zone and defines as the surface area needed to understand the subsurface geological model. (b) Schematic representation of geology with the definition of uncertainty in geological boundaries. Level-1 it is the direct observation from outcrops and galleries. Level-2 it is geological boundaries interpretation in and around outcrops and between galleries. Level-3 it is the geological boundaries interpretation within 100m from direct observation. Level-4 it is geological boundaries interpretation beyond 100m from direct observation. Level-5 it is the eroded interpretation of geology needed to understand the subsurface geological model.

You can access our models and dataset or apply your geological model, form visualising to classification.
With geoclass you can perform complex 3D processing operations and visualise your uncertainty classification. For example, you can:

1. Load your 3D geological model from disk.
2. Visualise your 3D geological model using point clouds.
3. Create uncertainty zones around your structural interpretation.
4. Classify your interpretation by level 1, 2, 3, 4 and 5.
5. Visualise the risk in your subsurface structural interpretation.
6. Get output file with the class you like to continue the further investigation.

# Zones
1. Zone-1 represent direct observation from outcrops and galleries.
2. Zone-2 show the area or space between galleries and around outcrops.
3. Zone-3 show interpretation which filled the space within 100m from direct observation.
4. Zone-4 show interpretation zone which filled the space beyond 100m from direct observation.
5. Zone-5 show surface interpretation zone which filled the space above the Earth’s surface, projected in the air for eroded or covered geology.

# Levels
1. Level-1 define as the parts of the horizons that directly collect from outcrops, coalmine galleries or boreholes. Plus direct faults observations.
2. Level-2 geological boundaries which are the verified parts of the horizons between the galleries and around the outcrops. Plus the secured faults interpretations.
3. Level-3 represent the parts of the horizons that projected due to nearby excavations or boreholes up to a distance of approximately 100 m).
4. Level-4 is subsurface observations in areas beyond 100m of direct observation.
5. Level-5 surface geological boundaries represent the interpretation parts above the Earth’s surface for covered or eroded geology. Plus the presumed faults interpretation.

# Requirements
• Python 3.8.5
• Jupyter notebook
• Suitable geoscience environment e.g. geoclass
#conda create --name geoclass anaconda
#conda activate geoclass

# Run locally - recommended
Set up Python, download the notebook and install the required libraries. We recommend using the Conda or pip of Python.
# Using free online resources
Run-on Colab (Google's cloud infrastructure), Run-on Binder or Run-on Kaggle. However, many online resources don't support the external window of Open 3D, so you need to use docker to solve the error.

# Dataset
The geological dataset used in this tutorial is a high-resolution dataset on CSV format. We will provide 3D models to run the code. This dataset from late Carboniferous multi-layered stratigraphy through the Ruhr basin, coal measures of Germany.

Link to dataset https://drive.google.com/drive/folders/1j4PBXQyVx89rkVTvMS7Yjl7e7y5OTDrC?usp=sharing
Link to dataset https://drive.google.com/drive/folders/1EabQCWqC1JExdLTRCJRx8MDAGHAhHy5N?usp=sharing
For more information about the dataset see
https://github.com/RamySaleem/Digitisation-2D-Sections-From-Scan-Images


# Visualise dataset
We have created an automated uncertainty classification workflow that expands the analysis into 3D space rather than based purely on 2D cross-section lines. Our automated uncertainty classifier Geoclass is open source and freely available. It shows examples of input and output files alongside 3D geological model and uncertainty zones and level visualisations. The automated approach aims to increase efficiency, as well as to incorporate 3D spatial information. The latter is particularly useful for borehole data that is often spatially dispersed and may not lie precisely on 2D cross-sections. 

# Calculate zones and levels
Our central premise is that uncertainty in a geological interpretation increases with distance away from sites of direct observation, as proposed by Drozdzewski et al. (1980). Critically the choice of length-scale is dependent on the nature of the geological structure and the tolerance required for a particular application. In our particular example, direct observations are made in mine-workings spaced at intervals of tens to hundreds of metres with fold structures of amplitudes, according to the interpretations of Drozdzewski et al. (1980), of a few km. Our schematic section, used to illustrate our definitions (Fig above), is of a similar scale, and we use length-scales of hundreds of metres to define what we term here “uncertainty zones”.  

After creating a point cloud object from the data, I create a loop that iterates over each key in the geoclass dictionary. Each key reads a CSV file containing point cloud data, creates an Open3D point cloud object from the data, and assigns it to geoclass_pcd. Then, I create a sphere around the centre of geoclass_pcd and expand geoclass_pcd by adding the sphere points to each point in the original point cloud. The resulting point cloud is stored in expanded_pcd. Then computes the convex hull of both the expanded point cloud and the original point cloud and creates Open3D line set objects from each hull. The expanded hull is coloured cyan, and the original hull is coloured red. Then I define a function in_hull that determines whether a point is inside the hull using the Delaunay function from the scipy.spatial module. Then call in_hull for each point in the interprets_pc_pts array, first with the expanded hull and then with the original hull. If a point is inside the original hull, the corresponding element in the total_ans array is set to 1. If a point is inside the expanded hull, but not the original hull and no other condition has been met for that point, the corresponding element in the total_ans array is set to 3. If a point is not inside either hull and its z-coordinate is positive, and no other condition has been met for that point, the corresponding element in the total_ans array is set to 5.

# Output and Future work
Generate an output CSV file with all levels together and each level spatially on the interpretation. This files can be used as an input for any further investigation using machine learning (GAN). For example, part of the output (level-1 or perhaps level-1 & 2) can be used on machine learning/deep learning models as input to predict the remaining levels (3, 4 and 5).

# Reference
Andrews, B. J. et al., 2019. How do we see fractures? Quantifying subjective bias in fracture data collection. Solid Earth, European Geosciences Union, 10(1), p. 487–516.
Bond, C. E., 2015. Uncertainty in structural interpretation: Lessons to be learnt. Journal of Structural Geology, 74(1), pp. 185 - 200.
Bond, C. E., Johnson, G. & Ellis, J. F., 2015. Structural model creation: the impact of data type and creative space on geological reasoning and interpretation. Geological Society, London, Special Publications, 11(421), pp. 83-97.
Drozdzewski, G., 1980. Ruhr Carboniferous Depth Tectonics Investigation Project, Westphalia Krefeld : Geological State Office North Rhine.
Drozdzewski, G., 1983. Tectonics of the Ruhr District, illustrated by reflection seismic profiles In Seismic Expression of Structural Styles - a Picture and Work Atlas.. AAPG Studies in Geology, 1:7(15), pp. 134 - 341.
Drozdzewski, G., 1993. The Ruhr coal basin (Germany)" structural evolution of an autochthonous foreland basin. International Journal of Coal Geology, 23(02), pp. 231-250.
Giessen, F. W. et al., 1990. Geophysical imagery of geological structures along the central segment of the EGT. Crustal structure of the Rhenish Massif: results of deep seismic reflection lines DEKORP 2-North and 2-North-Q. Geologische Rundschau Journal, 79(3), pp. 523-566.
Lark, R., Mathers, S., Marchant, A. & Hulbert, A., 2014. An index to represent lateral variation of the confidence of experts in a 3-D geological model.. Proceedings of the Geologists' Association, 3(125), pp. 267 - 278.
Wellmann, J. F. & Regenauer-Lieb, K., 2012. Uncertainties Have a Meaning: Information Entropy as a Quality Measure for 3-D Geological Models. Tectonophysics, https://doi.org/10.1016/j.tecto.2011.05.001, 2012., 526-529(1), p. 207–216.
Wilson, C. G. v., Bond, C. E. & Shipley, T. F., 2019. How can geologic decision-making under uncertainty be improved?. Solid Earth, European Geosciences Union (EGU), 2(10), pp. 1469 - 1488.
Wrede, V., 2005. Thrusting in a folded regime: fold accommodation faults in the Ruhr basin, Germany. Journal of Structural Geology, 27(04), p. 789–803.


Acknowledgements 
=================
The work contained in this repositories contains work conducted during a PhD study undertaken as part of the Natural Environment Research Council (NERC) Centre for Doctoral Training (CDT) in Oil & Gas funded 50% through its National Productivity Investment Fund grant number NE/R01051X/1 and 50% by the University of Aberdeen through its PhD Scholarship Scheme. The support of both organisations is gratefully acknowledged. The work is reliant on Open-Source Python Libraries, particularly openCV, CV2, numpy, matplotlib, plotly and pandas and contributors to these are thanked, along with Jovian and GitHub for open access hosting of the Python scripts for the study.

![University of Aberdeen](https://pbs.twimg.com/profile_images/1572172791801061377/UPSWmPyN_400x400.jpg)

![NERC-CDT](https://nerc-cdt-oil-and-gas.ac.uk/wp-content/uploads/news/2015-news-NERC-funding.jpg)

![NERC](https://auracdt.hull.ac.uk/wp-content/uploads/2019/11/UKRI_NER_Council-Logo_Horiz-RGB.png)

![CDT](https://i.imgur.com/QDOhcN3.png)


