from setuptools import setup

config = {
    'include_package_data': True,
    'description': 'Reverse complement experiments',
    'download_url': 'https://github.com/kundajelab/revcomp_experiments',
    'version': '0.1.0.0',
    'packages': [''],
    'package_data': {'simdna.resources': ['encode_motifs.txt.gz', 'HOCOMOCOv10_HUMAN_mono_homer_format_0.001.motif.gz']},
    'setup_requires': [],
    'install_requires': ['simdna', 'numpy>=1.9', 'matplotlib', 'scipy'],
    'dependency_links': ['git+git://github.com/kundajelab/simdna.git@v0.4.3.1#egg=simdna'],
    'scripts': ['scripts/motif_density_and_position_sim.py'],
    'name': 'simdna'
}

if __name__== '__main__':
    setup(**config)
