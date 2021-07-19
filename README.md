# ACCESS-CM2-025 Ocean Component

This is the 0.25 degree Ocean model from the [ACCESS-OM2 model](https://github.com/COSIMA/025deg_jra55_iaf), adapated for use with the ACCESS-CM2 model.

The atmospheric forcing component of the model has been removed, and the ocean and ice namelists updated. 

The [COSIMA ACCESS-OM2 1 degree model](https://github.com/COSIMA/1deg_jra55_iaf) namelists were compared to the 1 degree ocean model from CM2, with ocean specific parameters retained, and any parameters required for a coupled model added.

The 1 degree ACCESS-OM2 model namelists were then compared to the 0.25 ACCESS-OM2 model, and any 0.25 specific changes were added.

The `scripts` subfolder contains a python script used to "patch" the namelist files with additions (subtractions). 
