# sidata.ai platform project

You can see here to know about the `sidata.ai` platform.

https://liuyuwei.github.io/sidata.ai/

# service-data-eda-analysis

This is the service which used [pandas-profiling](https://github.com/pandas-profiling/pandas-profiling) to do the data EDA.

## How to use it?

- Please use docker to start the service.
```bash
$ cd docker
$ ./docker_build_service.sh
$ ./docker_start_service.sh
```

- If you want to remove the service.
```bash
$ ./docker_remove_service.sh
```

- Swagger api website:

http://{ip-address}:8002/docs

## Version, author and other information:
- See the relation information in [setup file](setup.py).

## License
- See License file [here](LICENSE).