# General Functionality

Users can import their custom compounds into the workbench of ChemMine Tools by drawing structures in the browser, copy and paste, from local files, or from a PubChem search. Subsequently, the imported compounds can be submitted from the workbench to the different analysis services.

## Workbench Overview

All compound structure data are organized in the compound workbench of ChemMine Tools. The workbench interface allows users to add, edit and remove compounds, and to view compound structure images in batches and to submit them to the other online services (see below).

## Compound Import

To import compounds into the workbench, users can choose from the following five options:

### SMILES Import

Users can import compound structures in the standard SMILES format. An overview of this format can be found here: Wikipedia: Simplified molecular-input line-entry system. A more comprehensive definition can be found here: Daylight Chemical Information Systems: SMILES - A Simplified Chemical Language.

### Structural Drawing

Users can draw a chemical structure directly in the browser.

### SDF Import

Users can import compound structures in the standard SDF format. An overview of this format can be found here: Wikipedia: Chemical table file. A more comprehensive definition can be found here: BIOVIA CTfile formats.

### PubChem CID Import

Users can import compound structures directly from PubChem by typing or pasting in a list of PubChem CIDs (one per line).

### PubChem Search

Alternatively, users can search the PubChem database with text or structure similarity searches and upload the identified compounds interactively to the workbench by clicking the "Add to Workbench" menus.

## Viewing of Compounds in Batches

Once compounds are imported into the workbench, the user can view them in list form, and optionally display structure images alongside each compound. Additional functionalities of the workspace interface are: add/edit/delete options and interactive structure similarity searches against PubChem.
Format Interconversions

For reformatting purposes, all compounds imported into ChemMine Tools can be saved in SMILES or SDF formats. The "My Compounds" page contains buttons to download the entire workbench as single SMILES or SDF file. Clicking further to an individual compound page provides download links for single compounds.

## Search Overview

ChemMine Tools provides two powerful structural similarity search algorithms: EI and PubChem Fingerpint. EI Search is an ultra-fast search tool developed in house (Cao et. al. 2010). PubChem Fingerprint searching connects directly to the PubChem database, and therefore can return compounds only recently added to PubChem. Both tools accept five different types of input: SMILES strings, structural drawings, SDF, and similarity to existing compounds in the Workbench. PLEASE NOTE: The EI search tool has been temporarily disabled as we update it's database.

## Searching for Compounds Similar to Those in Workbench

After uploading compounds to the Workbench, browse to "My Compounds" and click "search similar compounds" next to your compound of choice (Fig. 2). This will send the SMILES string to the search tool where you can select either EI or PubChem Fingerprint search. Please note: the similarity search provided by PubChem uses substructure-based fingerprints, while the similarity tools in the clustering and similarity services of ChemMine Tools are based on atom pairs and maximum common substructures. For more details, please see the theory section at the end of this tutorial.

Each tool in ChemMine Tools is just a Linux command line script, which can be written in any language. A .yaml file describes the input and output formats to the server. To contribute a new tool: (1) fork our repository on GitHub, (2) add in your tool to /tools/tool_scripts, and (3) perform a pull request to our "develop" branch. Please look at a few of the existing tools as examples for how to write the script and .yaml files.

Tools should be added here: https://github.com/TylerBackman/chemminetools/tree/develop/tools/tool_scripts
