# Security Policy

## Reporting a Vulnerability  
`gen10` doesn't handle sensitive files of your operating system or its crucial components. However, you may be working with sensitive information (e.g., DNA sequences). For privacy reasons, `gen10` does not store any input information except when using the **iterate** or **alphafold_prediction** features.  

Please note that the integration with AlphaFold involves sending information via requests to the remote AlphaFold 2.0 API. For more details, please refer to their [official website](https://alphafold.ebi.ac.uk/api-docs).  

The `gen10` community takes security bugs seriously. We appreciate your efforts to responsibly disclose your findings and report any security issues to the code owner.  

To report a security issue, please use the GitHub Security Advisory **"Report a Vulnerability"** tab.  

We will respond with the next steps for addressing your report. After our initial reply, the security team will keep you updated on progress toward a resolution and a full announcement. We may request additional information or clarification as needed.  

## Supported Versions  
We currently support just one version (v1.0). In theory, this API will be continuously supported until one of the features or libraries it relies on ends support for a functionality.  

| Version | Supported          |  
| ------- | ------------------ |  
| 1.0     | ✅ |

## Learning More About Security  

To learn more about securing an Electron application, please refer to the [Electron security tutorial](https://www.electronjs.org/docs/latest/tutorial/security).
