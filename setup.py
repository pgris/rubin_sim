from setuptools import setup, find_packages


scm_version_template = """# Generated by setuptools_scm
__all__ = ["__version__"]

__version__ = "{version}"
"""

setup(
    name="rubin_sim",
    use_scm_version={
        "write_to": "rubin_sim/version.py",
        "write_to_template": scm_version_template,
    },
    scripts=[
        "bin/maf/addRun",
        "bin/maf/glance_dir",
        "bin/maf/maf_night_report",
        "bin/maf/scimaf_dir",
        "bin/maf/showMaf",
        "bin/maf/generate_ss",
        "bin/maf/run_moving_calc",
        "bin/maf/run_moving_fractions",
        "bin/maf/run_moving_join",
        "bin/movingObjects/makeLSSTobs",
        "bin/movingObjects/addSeds",
        "bin/movingObjects/generateCoefficients",
        "bin/rs_download_data",
        'bin/rs_download_sky'
    ],
    packages=find_packages(),
)
