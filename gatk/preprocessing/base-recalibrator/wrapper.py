__author__ = "Dohoon Lee"
__copyright__ = "Copyright 2018, Dohoon Lee"
__email__ = "dohlee.bioinfo@gmail.com"
__license__ = "MIT"


from os import path

from snakemake.shell import shell

# Extract log.
log = snakemake.log_fmt_shell(stdout=False, stderr=True)
# Extract parameters.
extra = snakemake.params.get('extra', '')
java_options = '--java-options ' + snakemake.params.get('java_options', '-Xmx32g')

# Extract required arguments.
input = snakemake.input.bam
reference = snakemake.input.reference
known_sites = snakemake.input.known_sites
known_sites_command = ' '.join(['--known-sites ' + known_site for known_site in known_sites])

output = snakemake.output[0]

# Execute shell command.
shell(
    "("
    "gatk "
    "{java_options} "
    "BaseRecalibrator "
    "--input {input} "
    "--reference {reference} "
    "{known_sites_command} "
    "--output {output} "
    "{extra}"
    ")"
    "{log}"
)
