# open3d09_install
open3d 0.9.0, easy install
# note
all 3rdparty source code such as eigen, pybind11 .etc, have already downloaded and unzipped to folder "3rdparty",
you only need to download source code [here](https://github.com/Noel-Gallagher-Highflyingbirds/open3d09_install/tags) and use cmd following to install open3d0.9 on your machine


# windows
we use vs2019 to compile

unzip open3d09_install.zip Manually
if you have a conda virtual environment
```bash
conda activate <your_env_name>
```

then use cmd following
```bash
cd open3d09_install
mkdir build
cd build
cmake -G "Visual Studio 16 2019" -A x64 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX="D:/carlos/Program Files/open3d09_install/" ..
cmake --build . --config Release --target ALL_BUILD
cmake --build . --config Release --target INSTALL
cmake --build . --config Release --target pip-package
cd lib/python_package/pip_package
pip install open3d-0.9.0.0-cp37-cp37m-win_amd64.whl
conda list
```
then you'll see open3d installed in your virtual environment


*D:/carlos/Program Files/open3d09_install/* is a path to install open3d09
