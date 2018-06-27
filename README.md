# Readme for LOFAR pipeline template for the LOFAR rest API 

This is a template to use for implementing a new pipeline into the LOFAR rest API (https://github.com/EOSC-LOFAR/lofar_workflow_api). 


## Implement your own pipeline in the LOFAR rest API using this template
1. Copy this template and rename the directories called "LOFAR_pipeline_template". Also replace "LOFAR_pipeline_template" in the setup.py. Replace it with a sensible name for your pipeline.

2. Implement the functions in "LOFAR_pipeline_template/__init__.py".
2.1 The give_version() function should return the version of the pipeline as a string
2.2 The give_argument_names() should return a list of strings. The strings are the names of the arguments/parameters needed by the pipeline to run.
2.3 Implement the run_pipeline(\*\*kargs). This function should run the pipeline in the background in anyway you want. The kargs variable is a dict with the keys as given by the give_argument_names() function and the corresponding values given by the user.

3. Use pip install to install your pipeline python package for the rest API.

4. In the rest API alter the pipeline_administrator.py (https://github.com/EOSC-LOFAR/lofar_workflow_api/blob/master/lofar_workflow_api/api/pipeline_administrator.py) in the following way
4.1 Add your pipeline package to the import (e.g. import pipeline1, pipeline2, <your pipeline>)
4.2 Add your pipeline to the dict in the get_available_pipelines() function. E.g.:
```python 
	def get_available_pipelines():
		return {pipeline1.give_name(): pipeline1, 
			pipeline2.give_name(): pipeline2,
			<your pipeline>.give_name(): <your pipeline>}
```

