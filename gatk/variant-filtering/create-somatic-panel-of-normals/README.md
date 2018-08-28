# CreateSomaticPanelOfNormals ([doc](https://software.broadinstitute.org/gatk/documentation/tooldocs/current/org_broadinstitute_hellbender_tools_walkers_mutect_CreateSomaticPanelOfNormals.php))

make a panel of normals for use with [Mutect2](../../mutect2)

## IO

- [*{normal_sample1}*\_for\_pon\_vcf.gz, *{normal_sample2}*\_for\_pon\_vcf.gz, ..] (From tumor-only [Mutect2](../../mutect2/tumor-only))-> pon.vcf.gz

## Example snakemake rule
```python
rule create_somatic_panel_of_normals:
    input:
        # Required input.
        # Try `expand`-ing your normal samples for PoN generation.
        ['normal1_for_pon_vcf.gz', 'normal2_for_pon_vcf.gz']
    output:
        'pon.vcf.gz'
    params:
        # Optional parameters. Omit if unused.
        extra = ''
    threads: 1
    wrapper:
        'http://dohlee-bio.info:9193/gatk/variant-filtering/create-somatic-panel-of-normals'

```
