> Editorial note (prepared 2026-09-30; ethics status updated 2026-10-23): this is a submission-preparation copy of the original blank instrument, not a new administration. Items, decision criteria, material order and blank response fields are preserved. Candidate display names have been replaced with P codes as in the manuscript; public papers and identity clues may still identify individuals. Browser buttons mentioned in the original text described the HTML working page; this Markdown copy contains no buttons. Ethics approval SEU-EC-2026-0059 was issued on 2026-10-19, covering the human evaluation and the analysis and publication of study materials. The formal evaluation reported here was completed on 2026-10-20 to 2026-10-23 (after approval); all participants gave written informed consent and authorized publication.

# V-E factual-support and collaboration-rationale verification

Recipient: reviewer in EDA or integrated circuits. Please independently complete 32 factual checks, then complete the collaboration-rationale checks for the 8 cards in your specialty.

Packet V-E | Materials version open-v1-human-20260928

Open the local file in a browser to fill it in. To pause, click “Export draft”; next time use “Load draft” to resume. When finished, click “Check and export results” and return only the exported JSON file to the organizer. The page does not upload answers to any server.

## Respondent registration

- meta.participant_name ｜ Respondent name (for organizer registration only)：________

- meta.completed_date ｜ Actual completion date：________

- meta.prior_exposure ｜ Prior exposure to this packet (none not seen; materials seen materials but not configurations or others' conclusions; results seen configurations or others' conclusions; unknown uncertain)：________

- meta.ai_use ｜ AI use for this task (none not used; format only formatting or grammar checking; other other, please specify in the process note)：________

- meta.process_note ｜ Process note (any other AI use or workflow requiring explanation)：________

- meta.expertise ｜ Professional background and relevant research experience：________

- meta.project_role ｜ Any role in developing this system, candidate screening or card rewriting? (no not involved; yes involved, please specify)：________

- meta.conflict ｜ Any direct collaboration, supervisor–student relationship or conflict of interest with authors of the papers in this packet? (no no known relationship; yes yes, please specify items; unknown currently uncertain)：________

- meta.conflict_detail ｜ Details of relationship or conflict and item identifiers：________

## Instructions

For each item, compare the Chinese factual statement, the English quotation and the exact title/abstract passage received by the model on that run. Check especially numbers, conditions, materials, tasks and team-versus-individual attribution.

F2: all substantive content is supported by the quotation. F1: part of the content is supported, but material is added or conditions are omitted. F0: the core content is unsupported or contradicted. FU: knowledge or materials are insufficient to judge.

For F1, F0 or FU, identify the problematic wording or missing information. No note is required for F2. Do not use external knowledge or other parts of the paper to repair an insufficient quotation.

Fill in independently. Before the first submission, do not discuss specific labels or view other reviewers' results or automated issue prompts. If an item exceeds your expertise, you may choose FU.

The following two examples are fictional training examples, not part of the actual papers or experimental data.

Example 1: the quotation is “The study compared two polymer coatings at room temperature and found lower friction for coating A under the tested conditions.” The statement is “The study found lower friction for coating A under room-temperature test conditions.” This may be judged F2; it does not extend to other temperatures or materials.

Example 2: the quotation is “The authors evaluated the algorithm on synthetic benchmark data.” The statement is “This author can now provide real production data to collaborators.” This may be judged F0; a research team's past test does not establish an individual's current data-availability.

## Part 1: factual-support verification

### F022 factual-support verification

The paper proposed a prerouting path-delay prediction framework using a Transformer network and a residual model, extracting placement-stage timing and physical information as sequential features and modeling path-delay residuals to calibrate the difference between prerouting and postrouting delay.

> In this paper, an efficient and accurate pre-routing path delay prediction framework is proposed by employing transformer network and residual model, where the timing and physical information at placement stage is extracted as sequence features while the residual of path delay is modeled to calibrate the mismatch between the pre- and post-routing path delay.

[Paper Pre-Routing Path Delay Estimation Based on Transformer and Residual Framework](https://doi.org/10.1109/asp-dac52403.2022.9712484)

**Title and abstract passage supplied on that run**

```text
Pre-Routing Path Delay Estimation Based on Transformer and Residual Framework
Timing estimation prior to routing is of vital importance for optimization at placement stage and timing closure. Existing wire- or net-oriented learning-based methods limits the accuracy and efficiency of prediction due to the neglect of the delay correlation along path and computational complexity for delay accumulation. In this paper, an efficient and accurate pre-routing path delay prediction framework is proposed by employing transformer network and residual model, where the timing and physical information at placement stage is extracted as sequence features while the residual of path delay is modeled to calibrate the mismatch between the pre- and post-routing path delay. Experimental results demonstrate that with the proposed framework, the prediction error of post-routing path delay is less than 1.68% and 3.12% for seen and unseen circuits in terms of rRMSE, which is reduced by 2.3~5.0 times compared with exiting learning-based method for pre-routing prediction. Moreover, this framework produces at least three orders of magnitude speedup compared with the traditional design flow, which is promising to guide circuit optimization with satisfying prediction accuracy prior to time-consuming routing and timing analysis.
```

- F022.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F022.note ｜ Basis for judgment or information needed：________

### F012 factual-support verification

The paper proposed LLMACD, an LLM-based automatic designer with embedded analog-circuit design knowledge, and designed a refined prompt manager to extract circuit representations, embed circuit knowledge and model the design process in a chain-of-thought workflow.

> This paper introduces LLMACD, a knowledge-embedded automation designer for analog circuit design based on large language models (LLMs). We design a refined prompt manager to extract circuit representation, embed circuit knowledge, and model the knowledge-intensive design process within a Chain-of-Thought (CoT) workflow.

[Paper LLMACD: An LLM-Based Analog Circuit Designer Driven by Behavior Parameters](https://doi.org/10.1109/iseda65950.2025.11101244)

**Title and abstract passage supplied on that run**

```text
LLMACD: An LLM-Based Analog Circuit Designer Driven by Behavior Parameters
Analog circuit design is traditionally dependent on extensive human expertise, making the process time consuming and labor intensive. This paper introduces LLMACD, a knowledge-embedded automation designer for analog circuit design based on large language models (LLMs). We design a refined prompt manager to extract circuit representation, embed circuit knowledge, and model the knowledge-intensive design process within a Chain-of-Thought (CoT) workflow. Leveraging LLMs’ in-context learning capabilities and high-quality human-annotated design experience, LLMACD derives transistor behavioral parameters by analyzing performance expressions in a human-like manner without complex iterative loops, thereby accelerating the design process. Experimental results demonstrate that LLMACD outperforms traditional iterative transistor sizing optimization methods, achieving faster design times and enhanced circuit performance, with performance gains of up to 2 times.
```

- F012.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F012.note ｜ Basis for judgment or information needed：________

### F031 factual-support verification

The study showed that the as-cast structure of continuously cast ingots consists of an iron matrix and a network of M2C eutectic carbides, substantially refined relative to ingots produced by mold casting.

> The results show that the as‐cast structure consists of iron matrix and networks of M2C eutectic carbides, which are greatly refined in the continuous casting ingot compared to the case of ingot by mould casting.

[Paper Solidification Microstructure of AISI M2 High Speed Steel Manufactured by the Horizontal Continuous Casting Process](https://doi.org/10.1063/1.3552523)

**Title and abstract passage supplied on that run**

```text
Solidification Microstructure of AISI M2 High Speed Steel Manufactured by the Horizontal Continuous Casting Process
In the present work, AISI M2 high speed steel is produced by the horizontal continuous casting process. The difference of solidification microstructure in ingots by mould casting and continuous casting has been examined by means of scanning electron microscope (SEM), electron back‐scatter diffraction (EBSD), transmission electron microscope (TEM) and high resolution electron microscope (HREM). The results show that the as‐cast structure consists of iron matrix and networks of M2C eutectic carbides, which are greatly refined in the continuous casting ingot compared to the case of ingot by mould casting. Meanwhile, the morphology of M2C eutectic carbides changes from the plate‐like shape into the fibrous one. Micro‐twining and stacking faults are observed in the plate‐like M2C, whereas they are rarely identified in the fibrous M2C. Based on the characteristic of morphology and microstructure, it is expected that the plate‐like M2C is a faceted phase while the fibrous M2C is a non‐faceted phase.
```

- F031.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F031.note ｜ Basis for judgment or information needed：________

### F027 factual-support verification

The paper proposed a multimodal model combining power-delivery-network, layout and netlist data, incorporating auxiliary and contrastive learning to capture differences among power-delivery networks, and experimented on open-source designs.

> To address this challenge, we propose a multimodal model that integrates PDN, layout, and netlist data. Additionally, we incorporate auxiliary and contrastive learning techniques to capture the differences across various PDNs. Extensive experiments on open-source designs demonstrate the superior performance of our model.

[Paper Pre-Routing Timing Estimation Considering Power Delivery Network](https://doi.org/10.1109/iseda65950.2025.11100758)

**Title and abstract passage supplied on that run**

```text
Pre-Routing Timing Estimation Considering Power Delivery Network
In recent years, the demand for fast and accurate pre-routing timing prediction is increasing. However, existing machine learning (ML)-based methods for predicting pre-routing timing often overlook the impact of power delivery networks (PDNs), which are critical to IR drop and routing congestion, limiting the effectiveness of these approaches in real-world circuit designs. To address this challenge, we propose a multimodal model that integrates PDN, layout, and netlist data. Additionally, we incorporate auxiliary and contrastive learning techniques to capture the differences across various PDNs. Extensive experiments on open-source designs demonstrate the superior performance of our model.
```

- F027.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F027.note ｜ Basis for judgment or information needed：________

### F026 factual-support verification

In offline mode, the work transformed the original discrete design space into a continuous space, built predictive models, performed parallel gradient optimization, and mapped results back to the discrete domain.

> In offline mode, it transforms the original discrete design space into a continuous space, builds predictive models, performs parallel gradient-based optimization, and maps the results back to the discrete domain.

[Paper DCTDSE: A Bimodal Design Space Exploration Flow via Discrete–Continuous Transformation](https://doi.org/10.1109/tcad.2025.3596538)

**Title and abstract passage supplied on that run**

```text
DCTDSE: A Bimodal Design Space Exploration Flow via Discrete–Continuous Transformation
The conservation core accelerator presents a promising avenue for improving the computational efficiency of specific applications. However, its design space is ultra-high-dimensional, significantly increasing the exploratory effort required to identify the optimal design across performance, power, and area metrics. Furthermore, the discrete nature of the microarchitecture space renders conventional search methods ineffective. To tackle these challenges, we propose the Discrete Continuous Transformation to speedup Design Space Exploration, namely DCTDSE. It can operate in either offline or online mode. In offline mode, it transforms the original discrete design space into a continuous space, builds predictive models, performs parallel gradient-based optimization, and maps the results back to the discrete domain. In the online mode, DCTDSE refines the models by iteratively resampling previously found solutions, thereby enhancing exploration quality while maintaining moderate runtime overhead. Experimental results indicate that DCTDSE achieves a 3.9× to 40× speedup over benchmark methods in offline mode. In online mode, it provides a 2.5× speedup, with a 21% reduction in exploration quality relative to the most accurate comparison method.
```

- F026.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F026.note ｜ Basis for judgment or information needed：________

### F029 factual-support verification

The review states that laser powder-bed fusion uses a fine laser beam as a heat source, producing a small melt pool and extremely rapid cooling, thereby suppressing grain growth, intermetallic precipitation and macroscopic segregation.

> Particularly, laser powder bed fusion (LPBF), one prevalent AM technique, utilizes a fine laser beam as heat source and results in tiny molten pool with extremely fast cooling rate, which effectively restricts grain growth, inter-metallic precipitation and macroscopic segregation, thus facilitating the fabrication of high-performance metal parts.

[Paper Laser powder bed fusion of biodegradable magnesium alloys: process, microstructure and properties](https://doi.org/10.1088/2631-7990/ad967e)

**Title and abstract passage supplied on that run**

```text
Laser powder bed fusion of biodegradable magnesium alloys: process, microstructure and properties
Abstract Magnesium (Mg) alloys have gained recognition as revolutionary biomaterials, owing to their inherent degradability, favorable biocompatibility and mechanical properties. Additive manufacturing (AM) provides high design flexibility and enables the creation of implants with personalized complex shapes and internal porous structures tailored to individual anatomical and functional needs. Particularly, laser powder bed fusion (LPBF), one prevalent AM technique, utilizes a fine laser beam as heat source and results in tiny molten pool with extremely fast cooling rate, which effectively restricts grain growth, inter-metallic precipitation and macroscopic segregation, thus facilitating the fabrication of high-performance metal parts. This review critically assesses the significance of biodegradable Mg alloys and investigates the feasibility of utilizing LPBF for Mg alloys applications in biomedical field. Detailed discussions on LPBF-processed biomedical Mg alloys parts cover process parameters, microstructure, metallurgical defects, and properties like mechanical performance, corrosion behavior, and biological response in both as-built and post-processed states. Additionally, suggestions for advancing knowledge in LPBF of biodegradable Mg alloys for biomedical applications are highlighted to propel further research and development in this field.
```

- F029.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F029.note ｜ Basis for judgment or information needed：________

### F002 factual-support verification

The review compiled the mechanical properties of four additively manufactured metals, including Ti6Al4V, under monotonic tension and low-cycle fatigue, and examined the effects of anisotropy, surface treatment, heat treatment and other post-processing.

> This paper compiles the mechanical properties of four materials—Ti6Al4V, 17-4PH, 304 stainless steel, and 316 stainless steel under both monotonic tensile loading and low-cycle fatigue conditions from published literatures. It examines the effects of anisotropy, surface treatment, heat treatment, and other post-processing methods on the mechanical properties of AM metals.

[Paper Overview of material constitutive law for additive manufacturing metal structures](https://doi.org/10.1007/s44285-025-00046-3)

**Title and abstract passage supplied on that run**

```text
Overview of material constitutive law for additive manufacturing metal structures
Abstract Metal materials play a significant role in civil and construction engineering, and additively manufactured (AM) metals are gaining attention as a complementary technology due to their benefits of reduced material waste and greater design flexibility. In recent years, AM carbon steel, stainless steel, and alloy steel have drawn considerable interest from both academia and industry; however, their material properties are not yet fully understood. This paper compiles the mechanical properties of four materials—Ti6Al4V, 17-4PH, 304 stainless steel, and 316 stainless steel under both monotonic tensile loading and low-cycle fatigue conditions from published literatures. It examines the effects of anisotropy, surface treatment, heat treatment, and other post-processing methods on the mechanical properties of AM metals. Finally, this paper evaluates and compares the constitutive models for AM metals subjected to both monotonic tensile and low-cycle fatigue loading, providing insights to aid in the design and analysis of AM metal structures.
```

- F002.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F002.note ｜ Basis for judgment or information needed：________

### F018 factual-support verification

The study developed a two-dimensional cellular-automaton/finite-difference/CALPHAD model to simulate microstructure formation and solute segregation during solidification of ternary alloys.

> In this study, a two-dimensional (2D) cellular automaton (CA)-finite difference (FD)-CALPHAD model was developed to simulate the formation of microstructure and solute segregation in the solidification processes of ternary alloys.

[Paper Modeling of microstructure and microsegregation evolution in solidification of ternary alloys](https://doi.org/10.1088/1674-1056/adb8b5)

**Title and abstract passage supplied on that run**

```text
Modeling of microstructure and microsegregation evolution in solidification of ternary alloys
Abstract The microstructure formed during solidification has a significant impact on the mechanical properties of materials. In this study, a two-dimensional (2D) cellular automaton (CA)-finite difference (FD)-CALPHAD model was developed to simulate the formation of microstructure and solute segregation in the solidification processes of ternary alloys. In the model, dendritic growth is simulated using the CA technique, while solute diffusion is solved by the FD method, and the CALPHAD method is employed to calculate thermodynamic phase equilibrium during solidification. The CA-FD-CALPHAD coupled model is capable of reproducing the evolution of continuous nucleation and growth of grains as well as the evolution of the microstructure and solute distribution during solidification of ternary alloys. In this study, Al–Zn–Mg ternary alloy is taken as an example to simulate the growth of equiaxed and columnar grains and the columnar-to-equiaxed transition (CET) under different solidification conditions. The simulation results are compared with experimental data from the literature, showing a good agreement. Besides, the study also investigates the evolution of temperature and multicomponent solute fields during solidification and the effects of alloy composition and cooling rate on the microstructure morphology. The results reveal that the initial alloy composition and cooling rate significantly affect dendritic morphology and solute segregation. Higher initial alloy concentrations promote the growth of side branches in equiaxed grains, leading to more pronounced solute segregation between dendrites. As the cooling rate increases, the average grain size of the equiaxed grains decreases accordingly. Additionally, a higher cooling rate accelerates the columnar-to-equiaxed transition, leading to a finer grain structure.
```

- F018.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F018.note ｜ Basis for judgment or information needed：________

### F020 factual-support verification

The study proposed a two-relaxation-time lattice-Boltzmann model to simulate melt-pool flow, free-surface dynamics, solid–liquid phase change and heat transfer in electron-beam selective-melting additive manufacturing, and validated it with classical benchmarks.

> A two-relaxation-time lattice Boltzmann model is proposed to simulate melt flows and free surface dynamics in an EBSM additive manufacturing process. The model also describes the dynamics of solid-liquid phase change and heat transfer, and it is validated by several simulations of classical benchmarks.

[Paper A Two-Relaxation-Time Lattice Boltzmann Model for Electron Beam Selective Melting Additive Manufacturing](https://doi.org/10.3389/fmats.2022.885481)

**Title and abstract passage supplied on that run**

```text
A Two-Relaxation-Time Lattice Boltzmann Model for Electron Beam Selective Melting Additive Manufacturing
Electron beam selective melting is a rapidly developing additive manufacturing technology for industry and engineering. A two-relaxation-time lattice Boltzmann model is proposed to simulate melt flows and free surface dynamics in an EBSM additive manufacturing process. The model also describes the dynamics of solid-liquid phase change and heat transfer, and it is validated by several simulations of classical benchmarks. The model was applied to further simulate single and multiple tracks of electron beam selective melting on a single layer of powder bed and to analyze the influence of process parameters. The results demonstrate significant potentials of the present model for the study of additive manufacturing processes.
```

- F020.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F020.note ｜ Basis for judgment or information needed：________

### F011 factual-support verification

The paper proposed ChatChisel, a language-based agile hardware-design workflow using four LLM-based modules for decomposing, generating, correcting and composing hardware designs.

> We introduce ChatChisel, the first language-based agile hardware design workflow that generates Chisel from language specifications. ChatChisel utilizes four LLM-based modules for decomposing, generating, error-correcting, and composing hardware designs.

[Paper ChatChisel: Enabling Agile Hardware Design with Large Language Models](https://doi.org/10.1109/iseda62518.2024.10618053)

**Title and abstract passage supplied on that run**

```text
ChatChisel: Enabling Agile Hardware Design with Large Language Models
With the increasing complexity of integrated circuits, agile hardware design methodologies are crucial. Modern HDLs like Chisel enhance design quality, but manual implementations remain error-prone and time-consuming. Large language models (LLMs) offer potential for design automation through natural language but face challenges in generating large circuits using Verilog. We evaluate LLM capabilities for Chisel and Verilog generation, demonstrating superior Chisel generation ability. We introduce ChatChisel, the first language-based agile hardware design workflow that generates Chisel from language specifications. ChatChisel utilizes four LLM-based modules for decomposing, generating, error-correcting, and composing hardware designs. Techniques like LLM collaboration and RAG enhance ChatChisel's performance. Using GPT-3.5-turbo, we implemented an RV32I RISC-V CPU with 5-stage pipeline and dynamic branch prediction. We also validate our approach with extensive evaluations. Our experimental results reveal that ChatChisel can outperform LLM-based hardware design with Verilog by an average of 31.86%, implying a significant design capability enhancement and design process acceleration with ChatChisel.
```

- F011.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F011.note ｜ Basis for judgment or information needed：________

### F001 factual-support verification

The study constructed a multiscale model coupling macroscopic finite elements with microscopic cellular automata to simulate the temperature field and solidification microstructure of IN718 nickel superalloy during wire-arc additive manufacturing.

> A multiscale numerical model, integrating the macroscopic finite element model and the microscopic cellular automaton model, is developed to simulate temperature field distribution and solidification microstructure of IN718 nickel-based superalloy during wire arc additive manufacturing (WAAM).

[Paper Effects of near immersion active cooling on microstructure control in wire arc additive manufacturing of IN718: multiscale modeling and experiments](https://doi.org/10.1016/j.jmrt.2025.10.183)

**Title and abstract passage supplied on that run**

```text
Effects of near immersion active cooling on microstructure control in wire arc additive manufacturing of IN718: multiscale modeling and experiments
A multiscale numerical model, integrating the macroscopic finite element model and the microscopic cellular automaton model, is developed to simulate temperature field distribution and solidification microstructure of IN718 nickel-based superalloy during wire arc additive manufacturing (WAAM). Heat accumulation is shown to be intensified by geometric curvature, particularly in corner regions, and increases with layer number. By mapping macroscopic thermal field data into a two-dimensional quantitative cellular automaton model via multidimensional interpolation, the solidification and melting of microstructures are simulated. Simulated results agree well with experiments, confirming that the coarsest dendrites form in middle regions. A near immersion active cooling (NIAC) strategy is developed for the refinement of solidification microstructure. The application of the NIAC technique effectively enhances the heat dissipation and accelerates the cooling rates about 3.5 times, which thus suppresses thermal accumulation. In addition, NIAC significantly refines the primary dendrite arm spacing from 14.3-19.5 μm to 12.5-13.5 μm and reduces the volume fraction of Laves phase from 0.9%-1.7% to 0.6-1.1%. This study provides insights into the thermal–microstructural coupling in WAAM and demonstrates NIAC as an effective approach for microstructure control in WAAM of complex components.
```

- F001.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F001.note ｜ Basis for judgment or information needed：________

### F021 factual-support verification

The study used layout-generation techniques to create a large-scale layout dataset for extensive pretraining of a layout-understanding model, thereby alleviating data scarcity.

> To fully pre-train the layout understanding model (LUM), we create a large layout dataset using layout generation techniques, solving the data-hungry issues.

[Paper Bridging Hotspot Detection and Mask Optimization via Domain-Crossing Masked Layout Modeling](https://doi.org/10.1145/3728468)

**Title and abstract passage supplied on that run**

```text
Bridging Hotspot Detection and Mask Optimization via Domain-Crossing Masked Layout Modeling
With the rapid development of semiconductors, the size of transistors is continuously scaling down. The shrinking circuit size poses great challenges to optical proximity correction (OPC) and hotspot detection (HSD). Recent advancements in OPC and HSD commonly employ deep neural networks, achieving impressive performance within a limited runtime. Based on these achievements, we observe that deep-learning-based models of both HSD and OPC require knowledge of layout structure information. Furthermore, these two tasks are closely related to the lithography process during chip manufacturing. Observing such strong relationships, we propose that integrating OPC and HSD into a unified deep learning model will contribute to the performance of both tasks. To bridge the relationship between OPC and HSD, we first pre-train a layout understanding model built on the mask modeling technique, which effectively captures the layout geometric information, and then the pre-trained model can be easily fine-tuned on HSD and OPC with limited data. To fully pre-train the layout understanding model (LUM), we create a large layout dataset using layout generation techniques, solving the data-hungry issues. Experimental results show that the fine-tuned LUM model achieves remarkable performance on both OPC and HSD tasks.
```

- F021.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F021.note ｜ Basis for judgment or information needed：________

### F024 factual-support verification

The paper advocates developing multimodal circuit-representation learning to provide comprehensive understanding by harmonizing and extracting insights from data sources including functional specifications, RTL designs, circuit netlists and physical layouts.

> Pivotal to this vision is the development of a multimodal circuit representation learning technique, poised to provide a comprehensive understanding by harmonizing and extracting insights from varied data sources, such as functional specifications, register-transfer level (RTL) designs, circuit netlists, and physical layouts.

[Paper Large circuit models: opportunities and challenges](https://doi.org/10.1007/s11432-024-4155-7)

**Title and abstract passage supplied on that run**

```text
Large circuit models: opportunities and challenges
Abstract Within the electronic design automation (EDA) domain, artificial intelligence (AI)-driven solutions have emerged as formidable tools, yet they typically augment rather than redefine existing methodologies. These solutions often repurpose deep learning models from other domains, such as vision, text, and graph analytics, applying them to circuit design without tailoring to the unique complexities of electronic circuits. Such an “AI4EDA” approach falls short of achieving a holistic design synthesis and understanding, overlooking the intricate interplay of electrical, logical, and physical facets of circuit data. This study argues for a paradigm shift from AI4EDA towards AI-rooted EDA from the ground up, integrating AI at the core of the design process. Pivotal to this vision is the development of a multimodal circuit representation learning technique, poised to provide a comprehensive understanding by harmonizing and extracting insights from varied data sources, such as functional specifications, register-transfer level (RTL) designs, circuit netlists, and physical layouts. We champion the creation of large circuit models (LCMs) that are inherently multimodal, crafted to decode and express the rich semantics and structures of circuit data, thus fostering more resilient, efficient, and inventive design methodologies. Embracing this AI-rooted philosophy, we foresee a trajectory that transcends the current innovation plateau in EDA, igniting a profound “shift-left” in electronic design methodology. The envisioned advancements herald not just an evolution of existing EDA tools but a revolution, giving rise to novel instruments of design-tools that promise to radically enhance design productivity and inaugurate a new epoch where the optimization of circuit performance, power, and area (PPA) is achieved not incrementally, but through leaps that redefine the benchmarks of electronic systems’ capabilities.
```

- F024.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F024.note ｜ Basis for judgment or information needed：________

### F007 factual-support verification

The study validated the proposed preplacement timing-prediction and optimization framework using ISCAS'89, OpenCores and Gaisler benchmark circuits in TSMC 22 nm technology.

> The proposed pre-placement timing prediction and optimization framework was validated under TSMC 22nm process with the ISCAS’89, OpenCores, and Gaisler benchmark circuits.

[Paper Physical-Aware Multicorner Timing Prediction for Pre-Placement Optimization Using BiLSTM and GNN Networks](https://doi.org/10.1109/tcad.2025.3646591)

**Title and abstract passage supplied on that run**

```text
Physical-Aware Multicorner Timing Prediction for Pre-Placement Optimization Using BiLSTM and GNN Networks
The timing inpredictability at early design stage poses significant challenge to design convergence of integrated circuits, especially under multiple PVT corners. Prior works have concentrated exclusively on research of timing correlation and the related impact to circuit design across multiple design stages or corners, without addressing the influence of both on the final prediction accurately and efficiently. In this work, a physical aware timing prediction framework for multiple corners is proposed for pre-placement prediction and optimization by employing the bidirectional LSTM network and MLP network to learn the correlation from the sequence features and global features at logic synthesis stage, in which a GNN-based model is utilized to estimate the HPWL as physical feature, addressing the timing prediction challenge suffering from physical information absence. Besides, a corner selection mechanism is introduced to reduce the post-synthesis feature extraction overhead from multiple corners. The proposed pre-placement timing prediction and optimization framework was validated under TSMC 22nm process with the ISCAS’89, OpenCores, and Gaisler benchmark circuits. Significant prediction accuracy improvement is achieved to estimate the post-placement path delay for 12 PVT corners by post-synthesis timing analysis results under 5 corners with an average rRMSE of 8.75% for unseen designs, demonstrating a 19×∼53× runtime speedup. Significant placement quality improvement is achieved in terms of 25.96% ADP reduction and 20.52% PDP reduction in average compared to traditional design flow.
```

- F007.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F007.note ｜ Basis for judgment or information needed：________

### F004 factual-support verification

The paper proposed a multimodal-learning framework for optimization-aware prerouting timing prediction, using graph neural networks and convolutional neural networks to extract local netlist and layout information, respectively, and a Transformer to extract global path information.

> In this work, an optimization-aware prerouting timing prediction framework based on multimodal learning is proposed to calibrate the timing changes between placement and routing stages, where the local netlist and layout information are extracted by graph neural network (GNN) and convolutional neural network (CNN), respectively, while the global information along the path is further extracted by Transformer network.

[Paper An Optimization-Aware Prerouting Timing Prediction Framework Based on Multimodal Learning](https://doi.org/10.1109/tcad.2025.3547806)

**Title and abstract passage supplied on that run**

```text
An Optimization-Aware Prerouting Timing Prediction Framework Based on Multimodal Learning
Accurate and efficient prerouting timing estimation is particularly crucial during placement to alleviate time-consuming design iterations. Machine-learning (ML)-based methods have been introduced recently to predict the post-routing timing results at placement stage, but most of them neglect the impact of timing optimization during physical design, suffering from accuracy loss due to inconsistent circuit netlist. In this work, an optimization-aware prerouting timing prediction framework based on multimodal learning is proposed to calibrate the timing changes between placement and routing stages, where the local netlist and layout information are extracted by graph neural network (GNN) and convolutional neural network (CNN), respectively, while the global information along the path is further extracted by Transformer network. Based on the predicted post-routing timing results by the proposed framework, timing optimization guidance is generated to enhance traditional design flow with better physical implementation quality. Experimental results demonstrate that for the OpenCores benchmark circuits under TSMC 22nm process, the proposed framework achieves significant correlation and accuracy improvement with an average of 0.9219 in terms of R2 score and 2.12% of mean absolute percentage error (MAPE) as well as an average runtime acceleration of$645\times $compared with traditional design flow on testing designs. With the timing optimization guidance, significant worst negative slack (WNS) and total negative slack (TNS) improvement are achieved compared with traditional flow after placement and routing, respectively, without noticeable area, power, wire length, and the number of design rule check (DRC) violations increase.
```

- F004.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F004.note ｜ Basis for judgment or information needed：________

### F030 factual-support verification

By systematically optimizing the high-entropy-alloy content, the study obtained a lamellar dual-phase microstructure. Interaction between refined alpha-prime martensite and metastable beta promoted a progressive TRIP effect, enhancing strain hardening and stress redistribution.

> By systematically optimizing the HEA content, a lamellar dual-phase microstructure is achieved. The interplay between the refined α’ martensitic phase and the metastable β phase promotes a progressive transformation-induced plasticity (TRIP) effect, enabling superior strain hardening and stress redistribution.

[Paper Enhancing strength and ductility in Ti64 Alloys: Optimizing dual-phase heterostructures and TRIP effects via high-entropy alloy content modulation](https://doi.org/10.1016/j.matdes.2025.114399)

**Title and abstract passage supplied on that run**

```text
Enhancing strength and ductility in Ti64 Alloys: Optimizing dual-phase heterostructures and TRIP effects via high-entropy alloy content modulation
• Introduced an innovative in-situ multi-alloying strategy combining Ti64 with high-entropy alloy (HEA) CoCrFeNiMn. • Achieved a 37.5% increase in ultimate tensile strength and 140% improvement in elongation compared to conventional Ti64. • Developed a bimodal microstructure of ultrafine α′ martensite and metastable β phase. • Demonstrated progressive TRIP effect for improved work hardening. The mechanical performance of Ti-6Al-4 V (Ti64) alloys fabricated via Laser Powder Bed Fusion (L-PBF) can be significantly influenced by the addition of high-entropy alloy (HEA) particles. This study investigates the impact of varying HEA content on the microstructure and mechanical properties of Ti64 alloys. By systematically optimizing the HEA content, a lamellar dual-phase microstructure is achieved. The interplay between the refined α’ martensitic phase and the metastable β phase promotes a progressive transformation-induced plasticity (TRIP) effect, enabling superior strain hardening and stress redistribution. The Ti64-(3.0 wt%) HEA alloy achieves an ultimate tensile strength of 1438.1 MPa and elongation of 9.0 %, representing an optimal balance of strength and ductility.
```

- F030.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F030.note ｜ Basis for judgment or information needed：________

### F009 factual-support verification

The paper proposed a learning-driven, physically aware gate-sizing framework, constructing a multimodal gate-sizing-aware timing model by jointly learning timing information from multiple timing paths and physical information from multiscale layouts.

> In this work, we propose a learning-driven physically aware gate sizing framework to optimize timing performance on large-scale circuits efficiently. In our gradient descent optimization-based work, for obtaining accurate gradients, a multimodal gate sizing-aware timing model is achieved via learning timing information on multiple timing paths and physical information on multiple-scaled layouts jointly.

[Paper Learning-Driven Physically Aware Large-Scale Circuit Gate Sizing](https://doi.org/10.1109/tcad.2024.3488577)

**Title and abstract passage supplied on that run**

```text
Learning-Driven Physically Aware Large-Scale Circuit Gate Sizing
Gate sizing plays an important role in timing optimization after physical design. Existing machine learning-based gate sizing works cannot optimize timing on multiple timing paths simultaneously and neglect the physical constraint on layouts. They cause suboptimal sizing solutions and low-efficiency issues when compared with commercial gate sizing tools. In this work, we propose a learning-driven physically aware gate sizing framework to optimize timing performance on large-scale circuits efficiently. In our gradient descent optimization-based work, for obtaining accurate gradients, a multimodal gate sizing-aware timing model is achieved via learning timing information on multiple timing paths and physical information on multiple-scaled layouts jointly. Then, gradient generation based on the sizing-oriented estimator and adaptive back-propagation are developed to update gate sizes. Our results demonstrate that our work achieves higher-timing performance improvements in a faster way compared with the commercial gate sizing tool.
```

- F009.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F009.note ｜ Basis for judgment or information needed：________

### F010 factual-support verification

The study proposed a deep-neural-network architecture using a residual network for phase-formation prediction in high-entropy alloys and reported an overall accuracy of 81.9%.

> In this work, a deep neural network (DNN) structure using a residual network (RESNET) is proposed for the phase formation prediction of HEAs. It shows a high overall accuracy of 81.9%.

[Paper Phase formation prediction of high-entropy alloys: a deep learning study](https://doi.org/10.1016/j.jmrt.2022.01.172)

**Title and abstract passage supplied on that run**

```text
Phase formation prediction of high-entropy alloys: a deep learning study
High-entropy alloys (HEAs) represent prospective applications considering their outstanding mechanical properties. The properties in HEAs can be affected by the phase structure. Artificial neural network (ANN) is a promising machine learning approach for predicting the phases of HEAs. In this work, a deep neural network (DNN) structure using a residual network (RESNET) is proposed for the phase formation prediction of HEAs. It shows a high overall accuracy of 81.9%. Compared it with machine learning models, e.g., ANN and conventional DNN, its Micro-F1 score highlights the advantages of phase prediction of HEAs. It can remarkably prevent network degradation and improve the algorithm accuracy. It delivers a new path to develop the phase formation prediction model using deep learning, which can be of universal relevance in assisting the design of the HEAs with novel chemical compositions.
```

- F010.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F010.note ｜ Basis for judgment or information needed：________

### F015 factual-support verification

The review highlights advances including generative-adversarial-network data augmentation, active-learning loops for targeted experiments, and hybrid machine-learning/physics models incorporating strengthening mechanisms.

> In addition, frontier developments, such as the generative adversarial network (GAN)‐based data augmentation to tackle the issue of limited datasets, active learning loops for targeted experimentation, and hybrid ML‐physics models that incorporate fundamental strengthening mechanisms, are emphasized.

[Paper A Mini Review on Evolution of High‐Entropy Alloy Design: From Experimental Approaches to Machine Learning Integration](https://doi.org/10.1002/rar2.70048)

**Title and abstract passage supplied on that run**

```text
A Mini Review on Evolution of High‐Entropy Alloy Design: From Experimental Approaches to Machine Learning Integration
ABSTRACT High‐entropy alloys (HEAs) have emerged as a transformative class of materials distinguished by their complex chemical compositions, unique microstructures, and remarkable mechanical and functional properties. Traditionally, the discovery and optimization of HEAs have relied on conventional methods, including trial‐and‐error experimentation, first‐principles calculations, molecular dynamics (MD), and CALculation of PHAse Diagrams (CALPHAD). Although these techniques have contributed immensely to the discovery of HEAs, they struggle to efficiently and accurately navigate the vast and complex compositional space of HEAs owing to their inherent limitations. This review presents the evolution of HEA design methodologies, with a key focus on the paradigm shift brought about by the integration of machine learning (ML) into the HEA discovery process. It unifies composition design, phase prediction, microstructure analysis, and property/process optimization within a single coherent framework. In addition, frontier developments, such as the generative adversarial network (GAN)‐based data augmentation to tackle the issue of limited datasets, active learning loops for targeted experimentation, and hybrid ML‐physics models that incorporate fundamental strengthening mechanisms, are emphasized. Efforts to address persistent challenges include the use of local interpretable model‐agnostic explanation (LIME) and SHapley Additive exPlanations (SHAP), alongside physics‐informed approaches, to improve model interpretability, whereas Bayesian‐based techniques are utilized to improve uncertainty quantification. The synergy between experimental, computational, and data‐driven approaches is highlighted as a key driver for creating predictive alloy‐design frameworks that are both efficient and physically interpretable. By bridging conventional and data‐driven approaches, this study not only deepens the understanding of HEA design principles but also outlines how emerging ML strategies are poised to accelerate the transition from material conception to application. An outlook on next‐generation ML‐driven HEA design is presented, with an emphasis on addressing current limitations and leveraging recent breakthroughs to expand the frontiers of material discovery.
```

- F015.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F015.note ｜ Basis for judgment or information needed：________

### F003 factual-support verification

The study developed a multiphysics framework integrating discrete-element, finite-volume/volume-of-fluid and phase-field methods to simulate key phenomena including powder melting, melt-pool flow and directional solidification.

> By integrating the discrete element method for powder bed generation, finite volume method with volume of fluid for melt pool behavior, and phase-field method for microstructural evolution, the critical physical phenomena, including powder melting, molten pool flow, and directional solidification were simulated.

[Paper Multi-physics modeling of laser melted magnesium alloy: Bridging melt pool dynamics to microstructure evolution](https://doi.org/10.1016/j.jma.2025.06.032)

**Title and abstract passage supplied on that run**

```text
Multi-physics modeling of laser melted magnesium alloy: Bridging melt pool dynamics to microstructure evolution
• A multi-physics framework integrating of DEM, FVM-VOF, and PFM is establish to resolve multi-scale LPBF-processed Mg alloy. • Semi-elliptical molten pool exhibits intense Marangoni convection at the front, transitioning subdued flow in rear regions. • Columnar dendrites progress through linear growth, instability, competitive growth, and stabilization, governed by G and R . • Elevated P , combined with low V , promotes coarsen dendrites and homogenizes solutes. Laser powder bed fusion (LPBF) has revolutionized modern manufacturing by enabling high design freedom, rapid prototyping, and tailored mechanical properties. However, optimizing process parameters remains challenging due to the trial-and-error approaches required to capture subtle parameter-microstructure relationships. This study employed a multi-physics computational framework to investigate the melting and solidification dynamics of magnesium alloy. By integrating the discrete element method for powder bed generation, finite volume method with volume of fluid for melt pool behavior, and phase-field method for microstructural evolution, the critical physical phenomena, including powder melting, molten pool flow, and directional solidification were simulated. The effects of laser power and scanning speed on temperature distribution, melt pool geometry, and dendritic morphology were systematically analyzed. It was revealed that increasing laser power expanded melt pool dimensions and promoted columnar dendritic growth, while high scanning speeds reduced melt pool stability and refined dendritic structures. Furthermore, Marangoni convection and thermal gradients governed solute redistribution, with excessive energy input risking defects such as porosity and elemental evaporation. These insights establish quantitative correlations between process parameters, thermal history, and microstructural characteristics, providing a validated roadmap for LPBF-processed magnesium alloy with tailored performance.
```

- F003.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F003.note ｜ Basis for judgment or information needed：________

### F013 factual-support verification

The paper's MMCircuitEval benchmark contains 3,614 question–answer pairs covering key EDA stages from front-end to back-end design for digital and analog circuits.

> MMCircuitEval comprises 3614 meticulously curated question-answer (QA) pairs spanning digital and analog circuits across critical EDA stages—ranging from general knowledge and specifications to front-end and back-end design.

[Paper MMCircuitEval: A Comprehensive Multimodal Circuit-Focused Benchmark for Evaluating LLMs](https://doi.org/10.1109/iccad66269.2025.11240653)

**Title and abstract passage supplied on that run**

```text
MMCircuitEval: A Comprehensive Multimodal Circuit-Focused Benchmark for Evaluating LLMs
The emergence of multimodal large language models (MLLMs) presents promising opportunities for automation and enhancement in Electronic Design Automation (EDA). However, comprehensively evaluating these models in circuit design remains challenging due to the narrow scope of existing benchmarks. To bridge this gap, we introduce MMCircuitEval, the first multimodal benchmark specifically designed to assess MLLM performance comprehensively across diverse EDA tasks. MMCircuitEval comprises 3614 meticulously curated question-answer (QA) pairs spanning digital and analog circuits across critical EDA stages—ranging from general knowledge and specifications to front-end and back-end design. Derived from textbooks, technical question banks, datasheets, and real-world documentation, each QA pair undergoes rigorous expert review for accuracy and relevance. Our benchmark uniquely categorizes questions by design stage, circuit type, tested abilities (knowledge, comprehension, reasoning, computation), and difficulty level, enabling detailed analysis of model capabilities and limitations. Extensive evaluations reveal significant performance gaps among existing LLMs, particularly in back-end design and complex computations, highlighting the critical need for targeted training datasets and modeling approaches. MMCircuitEval provides a foundational resource for advancing MLLMs in EDA, facilitating their integration into real-world circuit design workflows. Our benchmark is available at https://github.com/cure-lab/MMCircuitEval.
```

- F013.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F013.note ｜ Basis for judgment or information needed：________

### F023 factual-support verification

The study validated the proposed framework through experimental evaluation, demonstrating successful transfer learning from 130 or 45 nm to 7 nm technology nodes.

> We validate the efficacy of our proposed framework through comprehensive experimental evaluations, demonstrating successful transfer learning from 130 or 45 to 7-nm technology nodes.

[Paper Prerouting Timing Prediction Across Different Technology Nodes](https://doi.org/10.1109/tcad.2024.3523426)

**Title and abstract passage supplied on that run**

```text
Prerouting Timing Prediction Across Different Technology Nodes
In the domain of very-large-scale integration (VLSI) design, the accuracy of prerouting timing prediction is of paramount importance for ensuring the performance and reliability of integrated circuits. Traditional methods based on machine learning necessitate the availability of extensive and high-quality datasets. However, this requirement poses significant challenges for advanced technology nodes due to the laborious and time-intensive nature of data preparation. To address this critical issue, we introduce a novel transfer learning framework that leverages data from preceding technology nodes to facilitate learning and prediction on the target node. Our methodology commences with the disentanglement and alignment of timing path features across different nodes, ensuring the preservation and effective translation of intrinsic timing path properties. Subsequently, we employ a Bayesian-based model to predict the arrival times of individual timing paths. This model is particularly adept at managing the high-variability inherent in arrival times and exhibits strong generalization capabilities to novel design scenarios. Moreover, we propose a new algorithm to reweight the preceding node data during training by estimating their transferability through the cell type distribution. We validate the efficacy of our proposed framework through comprehensive experimental evaluations, demonstrating successful transfer learning from 130 or 45 to 7-nm technology nodes. The results underscore the potential of our approach to significantly mitigate the dependency on extensive data preparation while maintaining high accuracy in timing prediction for cutting-edge VLSI designs.
```

- F023.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F023.note ｜ Basis for judgment or information needed：________

### F006 factual-support verification

The study proposed a learning-driven, physically aware gate-sizing framework for efficient timing optimization of large-scale circuits.

> In this work, we propose a learning-driven physically aware gate sizing framework to optimize timing performance on large-scale circuits efficiently.

[Paper Learning-Driven Physically Aware Large-Scale Circuit Gate Sizing](https://doi.org/10.1109/tcad.2024.3488577)

**Title and abstract passage supplied on that run**

```text
Learning-Driven Physically Aware Large-Scale Circuit Gate Sizing
Gate sizing plays an important role in timing optimization after physical design. Existing machine learning-based gate sizing works cannot optimize timing on multiple timing paths simultaneously and neglect the physical constraint on layouts. They cause suboptimal sizing solutions and low-efficiency issues when compared with commercial gate sizing tools. In this work, we propose a learning-driven physically aware gate sizing framework to optimize timing performance on large-scale circuits efficiently. In our gradient descent optimization-based work, for obtaining accurate gradients, a multimodal gate sizing-aware timing model is achieved via learning timing information on multiple timing paths and physical information on multiple-scaled layouts jointly. Then, gradient generation based on the sizing-oriented estimator and adaptive back-propagation are developed to update gate sizes. Our results demonstrate that our work achieves higher-timing performance improvements in a faster way compared with the commercial gate sizing tool.
```

- F006.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F006.note ｜ Basis for judgment or information needed：________

### F017 factual-support verification

The paper's ForgeEDA dataset includes multiple circuit representations: RTL code, post-mapping netlists, and-inverter graphs and placed netlists.

> ForgeEDA includes diverse circuit representations such as Register Transfer Level (RTL) code, Post-mapping (PM) netlists, And-Inverter Graphs (AIGs), and placed netlists, enabling comprehensive analysis and development.

[Paper ForgeEDA: A Comprehensive Multimodal Dataset for Advancing EDA](https://doi.org/10.1109/iseda65950.2025.11101194)

**Title and abstract passage supplied on that run**

```text
ForgeEDA: A Comprehensive Multimodal Dataset for Advancing EDA
We introduce ForgeEDA, an open-source comprehensive circuit dataset across various categories. ForgeEDA includes diverse circuit representations such as Register Transfer Level (RTL) code, Post-mapping (PM) netlists, And-Inverter Graphs (AIGs), and placed netlists, enabling comprehensive analysis and development. We demonstrate ForgeEDA’s utility by benchmarking state-of-the-art EDA algorithms on critical tasks such as Power, Performance, and Area (PPA) optimization, highlighting its ability to expose performance gaps and drive advancements. Additionally, ForgeEDA’s scale and diversity facilitate the training of AI models for EDA tasks, demonstrating its potential to improve model performance and generalization. By addressing limitations in existing datasets, ForgeEDA aims to catalyze breakthroughs in modern IC design and support the next generation of innovations in EDA.
```

- F017.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F017.note ｜ Basis for judgment or information needed：________

### F005 factual-support verification

By varying laser parameters, the study changed the microstructure of Ti64-CoCrFeNiMn alloy from beta-dominated to metastable beta plus nanoscale alpha-prime, substantially refining coarse acicular alpha-prime Ti and columnar beta Ti grains.

> By varying laser parameters, the resulting microstructure transitions from β-dominated to a metastable β + nanoscale α′ microstructure. The coarse needle-shaped α′-Ti and columnar β-Ti grains are significantly refined.

[Paper Achieving superior strength-ductility combination in the heterogeneous microstructured Ti64 alloy via multi-eutectoid elements alloying with CoCrFeNiMn during laser powder bed fusion](https://doi.org/10.1080/17452759.2024.2375106)

**Title and abstract passage supplied on that run**

```text
Achieving superior strength-ductility combination in the heterogeneous microstructured Ti64 alloy via multi-eutectoid elements alloying with CoCrFeNiMn during laser powder bed fusion
The formation of coarse needle-shaped α′-Ti within columnar β-Ti grains in additively manufactured titanium alloy components is nearly unavoidable, and it can lead to unforeseeable service failures. This study employs a multi-component eutectoid alloying strategy, integrating CoCrFeNiMn high-entropy alloy particles within Ti64 alloy. By varying laser parameters, the resulting microstructure transitions from β-dominated to a metastable β + nanoscale α′ microstructure. The coarse needle-shaped α′-Ti and columnar β-Ti grains are significantly refined. Concurrently, the multi-component eutectoid alloying strategy successfully suppresses the formation of detrimental intermetallic compounds by promoting the uniform distribution and solubility of the alloying elements. The Ti64-(4.5%) CoCrFeNiMn alloy demonstrates exceptional mechanical properties, including high tensile strength (1333.8 MPa), uniform elongation (9.3%), and a work-hardening capacity (>390.0 MPa). These are attributed to the continuous variation of Co, Cr, Fe, Ni, and Mn concentrations within the ultrafine α′ and metastable β-phase regions, providing a progressive transformation-induced plasticity effect.
```

- F005.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F005.note ｜ Basis for judgment or information needed：________

### F028 factual-support verification

The study proposed a deep-neural-network architecture that includes high-entropy-alloy manufacturing routes (as-cast and laser additive manufacturing) as input features and uses one-hot encoding to distinguish processing routes.

> To overcome these issues, in this work, a novel deep neural network architecture is proposed that includes HEA manufacturing routes as input features. The manufacturing routes, i.e., as-cast and laser additive manufactured samples, are transformed into the One-Hot encoder.

[Paper Machine Learning-Based Hardness Prediction of High-Entropy Alloys for Laser Additive Manufacturing](https://doi.org/10.1007/s11837-023-06174-x)

**Title and abstract passage supplied on that run**

```text
Machine Learning-Based Hardness Prediction of High-Entropy Alloys for Laser Additive Manufacturing
Abstract High-entropy alloys (HEAs) have attracted much attention for laser additive manufacturing, due to their superb mechanical properties. However, their industry application is still hindered by the high entry barriers of design for additive manufacturing and the limited performance library of HEAs. In most machine learning methods used to predict the properties of HEAs, their processing paths are not clearly distinguished. To overcome these issues, in this work, a novel deep neural network architecture is proposed that includes HEA manufacturing routes as input features. The manufacturing routes, i.e., as-cast and laser additive manufactured samples, are transformed into the One-Hot encoder. This makes the samples in the dataset provide better directivity and reduces the prediction error of the model. Data augmentation with conditional generative adversarial networks is employed to obtain some data samples with a distribution similar to that of the original data. These additional added data samples overcome the shortcoming of the limited performance library of HEAs. The results show that the mean absolute error value of the prediction is 44.6, which is about 27% lower than that using traditional neural networks in this work. This delivers a new path to discover chemical compositions suitable for laser additive manufactured HEAs, which is of universal relevance for assisting specific additive manufacturing processes.
```

- F028.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F028.note ｜ Basis for judgment or information needed：________

### F032 factual-support verification

The study established a multiscale numerical model coupling macroscopic finite elements with microscopic cellular automata to simulate temperature-field distribution and solidification microstructure during wire-arc additive manufacturing of IN718 nickel superalloy.

> A multiscale numerical model, integrating the macroscopic finite element model and the microscopic cellular automaton model, is developed to simulate temperature field distribution and solidification microstructure of IN718 nickel-based superalloy during wire arc additive manufacturing (WAAM).

[Paper Effects of near immersion active cooling on microstructure control in wire arc additive manufacturing of IN718: multiscale modeling and experiments](https://doi.org/10.1016/j.jmrt.2025.10.183)

**Title and abstract passage supplied on that run**

```text
Effects of near immersion active cooling on microstructure control in wire arc additive manufacturing of IN718: multiscale modeling and experiments
A multiscale numerical model, integrating the macroscopic finite element model and the microscopic cellular automaton model, is developed to simulate temperature field distribution and solidification microstructure of IN718 nickel-based superalloy during wire arc additive manufacturing (WAAM). Heat accumulation is shown to be intensified by geometric curvature, particularly in corner regions, and increases with layer number. By mapping macroscopic thermal field data into a two-dimensional quantitative cellular automaton model via multidimensional interpolation, the solidification and melting of microstructures are simulated. Simulated results agree well with experiments, confirming that the coarsest dendrites form in middle regions. A near immersion active cooling (NIAC) strategy is developed for the refinement of solidification microstructure. The application of the NIAC technique effectively enhances the heat dissipation and accelerates the cooling rates about 3.5 times, which thus suppresses thermal accumulation. In addition, NIAC significantly refines the primary dendrite arm spacing from 14.3-19.5 μm to 12.5-13.5 μm and reduces the volume fraction of Laves phase from 0.9%-1.7% to 0.6-1.1%. This study provides insights into the thermal–microstructural coupling in WAAM and demonstrates NIAC as an effective approach for microstructure control in WAAM of complex components.
```

- F032.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F032.note ｜ Basis for judgment or information needed：________

### F019 factual-support verification

The paper evaluated its PVT-Transfer framework on three integrated voltage references against four state-of-the-art circuit-sizing methods, using post-layout Monte Carlo simulation to validate performance superior to existing methods.

> The PVT-Transfer Framework is evaluated on three integrated voltage references and compared with four state-of-the-art circuit sizing methods. Based on post-layout Monte-Carlo simulations, this framework is verified to offer superior performance to existing methods

[Paper Knowledge Transfer Framework for PVT Robustness in Analog Integrated Circuits](https://doi.org/10.1109/tcsi.2023.3340683)

**Title and abstract passage supplied on that run**

```text
Knowledge Transfer Framework for PVT Robustness in Analog Integrated Circuits
Process, voltage, and temperature (PVT) variations in chip fabrication or operation pose a significant challenge to the robustness of analog integrated circuits. Existing design techniques for mitigating PVT variations involve analyzing offsets of DC operating points, but this approach often leads to compromises in circuit performance. To address this challenge, we developed a ‘PVT-Transfer’ framework to facilitate knowledge transfer with evolutionary design. Specifically, by cross-operating the circuit parameters under variations, design knowledge is transferred through parameter migration, thus enhancing the robustness of the resultant circuit. In addition, we leverage data-driven learning to discover potential similarities among PVT variations, thereby mitigating negative knowledge transfer. The PVT-Transfer Framework is evaluated on three integrated voltage references and compared with four state-of-the-art circuit sizing methods. Based on post-layout Monte-Carlo simulations, this framework is verified to offer superior performance to existing methods, yielding a 60% reduction in power consumption, an 80% increase in temperature resilience, and up to 70$\times$enhancement in the figure of merit. Further, it leads to a 60% reduction in the number of required circuit simulations and is suitable for parallel computation.
```

- F019.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F019.note ｜ Basis for judgment or information needed：________

### F008 factual-support verification

The study found that the water-quenching effect of underwater direct metal deposition refined the deposited material's grain size and increased dislocation density and lath-martensite content.

> The water quenching effect in the underwater direct metal deposition (UDMD) refined the grain size and increased the dislocation density and lath martensite content in the deposited material.

[Paper Underwater laser directed energy deposition of NV E690 steel](https://doi.org/10.1016/j.apmate.2022.100095)

**Title and abstract passage supplied on that run**

```text
Underwater laser directed energy deposition of NV E690 steel
Powder-based laser direct metal deposition (DMD), one of the directed energy deposition (DED) techniques, was applied in air and underwater to repair pre-machined NV E690 steel plates. Systematic investigations on the effects of the underwater environment and the ambient pressures (0.01 MPa–0.35 MPa) on the microstructure evolution, phase transformation, and mechanical properties were conducted. The water quenching effect in the underwater direct metal deposition (UDMD) refined the grain size and increased the dislocation density and lath martensite content in the deposited material. The theoretical models of the underwater pressurized nitriding process and the precipitation kinetics of (Ti, V) N particles were established. Moreover, the microstructure evolution and the mechanical properties of other UDMD repaired samples did not show obvious relation with the underwater ambient pressures. This investigation not only provides an efficient candidate for the underwater restoration technique but also bridges marine engineering and emerging DMD technology.
```

- F008.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F008.note ｜ Basis for judgment or information needed：________

### F014 factual-support verification

The review focuses on deposition-architecture strategies in wire-arc additive manufacturing of dissimilar alloys, analyzing how microstructural control affects the type, size and distribution of interfacial intermetallic compounds.

> This review focuses on deposition architecture strategies in wire arc additive manufacturing (WAAM) of dissimilar alloys, providing an in-depth analysis of how precise microstructure regulation affects the type, size, and distribution of interfacial IMCs.

[Paper Wire arc additive manufacturing of dissimilar alloys: Processing strategies and interfacial phenomena](https://doi.org/10.1016/j.jmapro.2025.10.079)

**Title and abstract passage supplied on that run**

```text
Wire arc additive manufacturing of dissimilar alloys: Processing strategies and interfacial phenomena
Dissimilar alloys additive manufacturing enables the tailored creation of heterogeneous microstructures with exceptional mechanical properties, significantly expanding the application boundaries of metallic materials and accelerating the convergence of materials science with advanced manufacturing technologies. However, the thermophysical property mismatch between dissimilar materials frequently induces intermetallic compounds (IMCs) formation at component interfaces, leading to cracking and structural failure. This review focuses on deposition architecture strategies in wire arc additive manufacturing (WAAM) of dissimilar alloys, providing an in-depth analysis of how precise microstructure regulation affects the type, size, and distribution of interfacial IMCs. Few systematic reviews on the complex interrelationships between the interfacial microstructural characteristics and mechanical properties of dissimilar alloys WAAM components exist. To address this, a comprehensive analysis of WAAM process parameters was carried out, deposition optimization strategies were explored, and the correlations between microstructure and properties across diverse dissimilar alloys systems were investigated. Furthermore, this work synthesizes recent breakthroughs in fabrication forming control and microstructure optimization for WAAM processed dissimilar alloys while prospectively discussing emerging opportunities and technical challenges to guide future research in this field.
```

- F014.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F014.note ｜ Basis for judgment or information needed：________

### F016 factual-support verification

The study integrated machine vision, three-dimensional reconstruction based on actual morphology and numerical simulation to rapidly calculate stress evolution during laser-directed energy deposition, establishing a mapping between deposited-layer surface shrinkage and stress.

> It integrates machine vision, three-dimensional reconstruction based on actual morphology, and numerical simulation to calculate rapidly stress development during the LDED process. Meanwhile, a mapping relationship between the surface shrinkage of the deposition layer and stress is established, providing a theoretical basis for the DCM.

[Paper Online stress monitoring during laser-directed energy deposition based on dynamic contour method](https://doi.org/10.1080/17452759.2024.2448543)

**Title and abstract passage supplied on that run**

```text
Online stress monitoring during laser-directed energy deposition based on dynamic contour method
Deformation and cracking caused by internal stress have been a long-standing challenge in the field of metal additive manufacturing. This paper presents a novel method for real-time stress assessment of laser-directed energy deposition (LDED) based on the shrinkage phenomenon of deposition layer – the Dynamic Contour Method (DCM). It integrates machine vision, three-dimensional reconstruction based on actual morphology, and numerical simulation to calculate rapidly stress development during the LDED process. Meanwhile, a mapping relationship between the surface shrinkage of the deposition layer and stress is established, providing a theoretical basis for the DCM. Regarding the validation of this method, the DCM simulations are compared with the experimentally calibrated thermo-mechanical coupling simulations. The results show a high degree of consistency, demonstrating the feasibility and accuracy of the DCM. This method provides a new digital twin framework for additive manufacturing.
```

- F016.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F016.note ｜ Basis for judgment or information needed：________

### F025 factual-support verification

The work experimented on ISCAS'89 benchmark circuits in TSMC 22 nm technology; the proposed framework achieved average critical-path prediction F1 scores of 95.0% and 93.6% on seen and unseen circuits, respectively.

> Experimental results demonstrate that with the proposed framework, the average prediction accuracy of critical paths achieves 95.0% and 93.6% for seen and unseen circuits in terms of F1-score for ISCAS’89 benchmark circuits under TSMC 22nm process

[Paper Critical Paths Prediction under Multiple Corners Based on BiLSTM Network](https://doi.org/10.1109/dac56929.2023.10247984)

**Title and abstract passage supplied on that run**

```text
Critical Paths Prediction under Multiple Corners Based on BiLSTM Network
Critical path generation poses significant challenge to integrated circuit (IC) design flow in terms of huge computational complexity and crucial impact to circuit optimization, whose early prediction is of vital importance for accelerating the design closure, especially under multiple process-voltage-temperature (PVT) corners. In this work, a post-routing critical path prediction framework is proposed based on Bidirectional Long Short-Term Memory (BiLSTM) network and Multi-Layer Perceptron (MLP) network to learn from the sequential features and global features at logic synthesis stage, which are extracted from the timing and physical information of cell sequences and operation conditions for circuit respectively. Experimental results demonstrate that with the proposed framework, the average prediction accuracy of critical paths achieves 95.0% and 93.6% for seen and unseen circuits in terms of F1-score for ISCAS’89 benchmark circuits under TSMC 22nm process, demonstrating an increase of 10.8% and 13.9% compared with existing learning-based critical paths prediction method.
```

- F025.status ｜ Your judgment (F2 fully supported; F1 partially supported; F0 unsupported or contradicted; FU unable to judge)：________

- F025.note ｜ Basis for judgment or information needed：________

## Part 2: collaboration-rationale verification

Read the collaboration rationale and items requiring confirmation in light of the original need, the listed facts and their sources. Judge whether a concrete collaboration entry point exists and whether material, task or method transfer conditions should be retained.

R2: a reasonable conditional suggestion. R1: the direction may hold but requires local revision. R0: the core link lacks support, contradicts the need or relies on a wrong premise. RU: current information is insufficient to judge.

Check whether the rationale adds constraints absent from the original need, attributes team results to an individual, writes “never addressed” about something not mentioned, or turns past research into a current resource commitment.

For R1, R0 or RU, add a one-sentence rationale. Issue types may be multi-selected; no long report is required.

Find complementary electronic design automation expertise for applying domain language models to chip design. Seek design task knowledge, real design data usable for research, and executable design-flow validation. Relevant tasks include timing, physical design and layout. Generated layouts and a paper's past access to a process library do not establish available, licensed real design data.

Find complementary electronic design automation expertise for applying domain language models to chip design. Seek design task knowledge, real design data usable for research, and executable design-flow validation. Relevant tasks include timing, physical design and layout. Generated layouts and a paper's past access to a process library do not establish available, licensed real design data.

### K006 Candidate P006

#### Research fact 1

The study validated the proposed framework through experimental evaluation, demonstrating successful transfer learning from 130 or 45 nm to 7 nm technology nodes.

> We validate the efficacy of our proposed framework through comprehensive experimental evaluations, demonstrating successful transfer learning from 130 or 45 to 7-nm technology nodes.

[Paper Prerouting Timing Prediction Across Different Technology Nodes](https://doi.org/10.1109/tcad.2024.3523426)

**Title and abstract passage supplied on that run**

```text
Prerouting Timing Prediction Across Different Technology Nodes
In the domain of very-large-scale integration (VLSI) design, the accuracy of prerouting timing prediction is of paramount importance for ensuring the performance and reliability of integrated circuits. Traditional methods based on machine learning necessitate the availability of extensive and high-quality datasets. However, this requirement poses significant challenges for advanced technology nodes due to the laborious and time-intensive nature of data preparation. To address this critical issue, we introduce a novel transfer learning framework that leverages data from preceding technology nodes to facilitate learning and prediction on the target node. Our methodology commences with the disentanglement and alignment of timing path features across different nodes, ensuring the preservation and effective translation of intrinsic timing path properties. Subsequently, we employ a Bayesian-based model to predict the arrival times of individual timing paths. This model is particularly adept at managing the high-variability inherent in arrival times and exhibits strong generalization capabilities to novel design scenarios. Moreover, we propose a new algorithm to reweight the preceding node data during training by estimating their transferability through the cell type distribution. We validate the efficacy of our proposed framework through comprehensive experimental evaluations, demonstrating successful transfer learning from 130 or 45 to 7-nm technology nodes. The results underscore the potential of our approach to significantly mitigate the dependency on extensive data preparation while maintaining high accuracy in timing prediction for cutting-edge VLSI designs.
```

#### Research fact 2

The study used layout-generation techniques to create a large-scale layout dataset for extensive pretraining of a layout-understanding model, thereby alleviating data scarcity.

> To fully pre-train the layout understanding model (LUM), we create a large layout dataset using layout generation techniques, solving the data-hungry issues.

[Paper Bridging Hotspot Detection and Mask Optimization via Domain-Crossing Masked Layout Modeling](https://doi.org/10.1145/3728468)

**Title and abstract passage supplied on that run**

```text
Bridging Hotspot Detection and Mask Optimization via Domain-Crossing Masked Layout Modeling
With the rapid development of semiconductors, the size of transistors is continuously scaling down. The shrinking circuit size poses great challenges to optical proximity correction (OPC) and hotspot detection (HSD). Recent advancements in OPC and HSD commonly employ deep neural networks, achieving impressive performance within a limited runtime. Based on these achievements, we observe that deep-learning-based models of both HSD and OPC require knowledge of layout structure information. Furthermore, these two tasks are closely related to the lithography process during chip manufacturing. Observing such strong relationships, we propose that integrating OPC and HSD into a unified deep learning model will contribute to the performance of both tasks. To bridge the relationship between OPC and HSD, we first pre-train a layout understanding model built on the mask modeling technique, which effectively captures the layout geometric information, and then the pre-trained model can be easily fine-tuned on HSD and OPC with limited data. To fully pre-train the layout understanding model (LUM), we create a large layout dataset using layout generation techniques, solving the data-hungry issues. Experimental results show that the fine-tuned LUM model achieves remarkable performance on both OPC and HSD tasks.
```

#### Collaboration rationale

If a domain language model is to be applied to timing prediction across technology nodes or layout understanding, this candidate's experience in transfer learning and layout modeling could be complementary. However, the data are generated or cross-node data; usability for real design tasks needs confirmation.

#### Items requiring confirmation

Establish whether the candidate can obtain real design data and technology-library licenses, has conditions for validating executable design flows, and is willing to collaborate.

- K006.status ｜ Your judgment (R2 reasonable conditional suggestion; R1 direction plausible but needs local revision; R0 insufficient basis or clearly unsuitable; RU unable to judge)：________

- K006.note ｜ Basis for judgment or information needed：________

- K006.flag_Demand drift ｜ Demand drift：________

- K006.flag_Personal attribution ｜ Personal attribution：________

- K006.flag_Unsupported negative claim ｜ Unsupported negative claim：________

- K006.flag_Transfer conditions ｜ Transfer conditions：________

- K006.flag_Resource or willingness commitment ｜ Resource or willingness commitment：________

### K007 Candidate P013

#### Research fact 1

The study proposed a learning-driven, physically aware gate-sizing framework for efficient timing optimization of large-scale circuits.

> In this work, we propose a learning-driven physically aware gate sizing framework to optimize timing performance on large-scale circuits efficiently.

[Paper Learning-Driven Physically Aware Large-Scale Circuit Gate Sizing](https://doi.org/10.1109/tcad.2024.3488577)

**Title and abstract passage supplied on that run**

```text
Learning-Driven Physically Aware Large-Scale Circuit Gate Sizing
Gate sizing plays an important role in timing optimization after physical design. Existing machine learning-based gate sizing works cannot optimize timing on multiple timing paths simultaneously and neglect the physical constraint on layouts. They cause suboptimal sizing solutions and low-efficiency issues when compared with commercial gate sizing tools. In this work, we propose a learning-driven physically aware gate sizing framework to optimize timing performance on large-scale circuits efficiently. In our gradient descent optimization-based work, for obtaining accurate gradients, a multimodal gate sizing-aware timing model is achieved via learning timing information on multiple timing paths and physical information on multiple-scaled layouts jointly. Then, gradient generation based on the sizing-oriented estimator and adaptive back-propagation are developed to update gate sizes. Our results demonstrate that our work achieves higher-timing performance improvements in a faster way compared with the commercial gate sizing tool.
```

#### Research fact 2

In offline mode, the work transformed the original discrete design space into a continuous space, built predictive models, performed parallel gradient optimization, and mapped results back to the discrete domain.

> In offline mode, it transforms the original discrete design space into a continuous space, builds predictive models, performs parallel gradient-based optimization, and maps the results back to the discrete domain.

[Paper DCTDSE: A Bimodal Design Space Exploration Flow via Discrete–Continuous Transformation](https://doi.org/10.1109/tcad.2025.3596538)

**Title and abstract passage supplied on that run**

```text
DCTDSE: A Bimodal Design Space Exploration Flow via Discrete–Continuous Transformation
The conservation core accelerator presents a promising avenue for improving the computational efficiency of specific applications. However, its design space is ultra-high-dimensional, significantly increasing the exploratory effort required to identify the optimal design across performance, power, and area metrics. Furthermore, the discrete nature of the microarchitecture space renders conventional search methods ineffective. To tackle these challenges, we propose the Discrete Continuous Transformation to speedup Design Space Exploration, namely DCTDSE. It can operate in either offline or online mode. In offline mode, it transforms the original discrete design space into a continuous space, builds predictive models, performs parallel gradient-based optimization, and maps the results back to the discrete domain. In the online mode, DCTDSE refines the models by iteratively resampling previously found solutions, thereby enhancing exploration quality while maintaining moderate runtime overhead. Experimental results indicate that DCTDSE achieves a 3.9× to 40× speedup over benchmark methods in offline mode. In online mode, it provides a 2.5× speedup, with a 21% reduction in exploration quality relative to the most accurate comparison method.
```

#### Collaboration rationale

If a domain language model is to be connected to physical-design and timing-optimization tasks, this candidate's experience in physically aware gate sizing and design-space exploration could be complementary. However, the methods target specific optimization objectives; compatibility with a language model and real flows needs confirmation.

#### Items requiring confirmation

Establish whether the candidate can provide real design data and executable design flows, the current licensing status of toolchains and technology libraries, and willingness to collaborate.

- K007.status ｜ Your judgment (R2 reasonable conditional suggestion; R1 direction plausible but needs local revision; R0 insufficient basis or clearly unsuitable; RU unable to judge)：________

- K007.note ｜ Basis for judgment or information needed：________

- K007.flag_Demand drift ｜ Demand drift：________

- K007.flag_Personal attribution ｜ Personal attribution：________

- K007.flag_Unsupported negative claim ｜ Unsupported negative claim：________

- K007.flag_Transfer conditions ｜ Transfer conditions：________

- K007.flag_Resource or willingness commitment ｜ Resource or willingness commitment：________

### K008 Candidate P014

#### Research fact 1

The paper proposed LLMACD, an LLM-based automatic designer with embedded analog-circuit design knowledge, and designed a refined prompt manager to extract circuit representations, embed circuit knowledge and model the design process in a chain-of-thought workflow.

> This paper introduces LLMACD, a knowledge-embedded automation designer for analog circuit design based on large language models (LLMs). We design a refined prompt manager to extract circuit representation, embed circuit knowledge, and model the knowledge-intensive design process within a Chain-of-Thought (CoT) workflow.

[Paper LLMACD: An LLM-Based Analog Circuit Designer Driven by Behavior Parameters](https://doi.org/10.1109/iseda65950.2025.11101244)

**Title and abstract passage supplied on that run**

```text
LLMACD: An LLM-Based Analog Circuit Designer Driven by Behavior Parameters
Analog circuit design is traditionally dependent on extensive human expertise, making the process time consuming and labor intensive. This paper introduces LLMACD, a knowledge-embedded automation designer for analog circuit design based on large language models (LLMs). We design a refined prompt manager to extract circuit representation, embed circuit knowledge, and model the knowledge-intensive design process within a Chain-of-Thought (CoT) workflow. Leveraging LLMs’ in-context learning capabilities and high-quality human-annotated design experience, LLMACD derives transistor behavioral parameters by analyzing performance expressions in a human-like manner without complex iterative loops, thereby accelerating the design process. Experimental results demonstrate that LLMACD outperforms traditional iterative transistor sizing optimization methods, achieving faster design times and enhanced circuit performance, with performance gains of up to 2 times.
```

#### Research fact 2

The paper evaluated its PVT-Transfer framework on three integrated voltage references against four state-of-the-art circuit-sizing methods, using post-layout Monte Carlo simulation to validate performance superior to existing methods.

> The PVT-Transfer Framework is evaluated on three integrated voltage references and compared with four state-of-the-art circuit sizing methods. Based on post-layout Monte-Carlo simulations, this framework is verified to offer superior performance to existing methods

[Paper Knowledge Transfer Framework for PVT Robustness in Analog Integrated Circuits](https://doi.org/10.1109/tcsi.2023.3340683)

**Title and abstract passage supplied on that run**

```text
Knowledge Transfer Framework for PVT Robustness in Analog Integrated Circuits
Process, voltage, and temperature (PVT) variations in chip fabrication or operation pose a significant challenge to the robustness of analog integrated circuits. Existing design techniques for mitigating PVT variations involve analyzing offsets of DC operating points, but this approach often leads to compromises in circuit performance. To address this challenge, we developed a ‘PVT-Transfer’ framework to facilitate knowledge transfer with evolutionary design. Specifically, by cross-operating the circuit parameters under variations, design knowledge is transferred through parameter migration, thus enhancing the robustness of the resultant circuit. In addition, we leverage data-driven learning to discover potential similarities among PVT variations, thereby mitigating negative knowledge transfer. The PVT-Transfer Framework is evaluated on three integrated voltage references and compared with four state-of-the-art circuit sizing methods. Based on post-layout Monte-Carlo simulations, this framework is verified to offer superior performance to existing methods, yielding a 60% reduction in power consumption, an 80% increase in temperature resilience, and up to 70$\times$enhancement in the figure of merit. Further, it leads to a 60% reduction in the number of required circuit simulations and is suitable for parallel computation.
```

#### Collaboration rationale

If a domain language model is to be applied to chip design, this candidate's LLM analog-circuit design flow and experience in post-layout simulation validation could contribute task knowledge and a flow-validation perspective. However, both concern analog circuits and do not involve timing or physical-design placement.

#### Items requiring confirmation

Establish whether the candidate understands digital timing/physical-design tasks, can provide real design data with permission for use, and is willing to participate in validating executable design flows.

- K008.status ｜ Your judgment (R2 reasonable conditional suggestion; R1 direction plausible but needs local revision; R0 insufficient basis or clearly unsuitable; RU unable to judge)：________

- K008.note ｜ Basis for judgment or information needed：________

- K008.flag_Demand drift ｜ Demand drift：________

- K008.flag_Personal attribution ｜ Personal attribution：________

- K008.flag_Unsupported negative claim ｜ Unsupported negative claim：________

- K008.flag_Transfer conditions ｜ Transfer conditions：________

- K008.flag_Resource or willingness commitment ｜ Resource or willingness commitment：________

### K001 Candidate P004

#### Research fact 1

The paper proposed a multimodal-learning framework for optimization-aware prerouting timing prediction, using graph neural networks and convolutional neural networks to extract local netlist and layout information, respectively, and a Transformer to extract global path information.

> In this work, an optimization-aware prerouting timing prediction framework based on multimodal learning is proposed to calibrate the timing changes between placement and routing stages, where the local netlist and layout information are extracted by graph neural network (GNN) and convolutional neural network (CNN), respectively, while the global information along the path is further extracted by Transformer network.

[Paper An Optimization-Aware Prerouting Timing Prediction Framework Based on Multimodal Learning](https://doi.org/10.1109/tcad.2025.3547806)

**Title and abstract passage supplied on that run**

```text
An Optimization-Aware Prerouting Timing Prediction Framework Based on Multimodal Learning
Accurate and efficient prerouting timing estimation is particularly crucial during placement to alleviate time-consuming design iterations. Machine-learning (ML)-based methods have been introduced recently to predict the post-routing timing results at placement stage, but most of them neglect the impact of timing optimization during physical design, suffering from accuracy loss due to inconsistent circuit netlist. In this work, an optimization-aware prerouting timing prediction framework based on multimodal learning is proposed to calibrate the timing changes between placement and routing stages, where the local netlist and layout information are extracted by graph neural network (GNN) and convolutional neural network (CNN), respectively, while the global information along the path is further extracted by Transformer network. Based on the predicted post-routing timing results by the proposed framework, timing optimization guidance is generated to enhance traditional design flow with better physical implementation quality. Experimental results demonstrate that for the OpenCores benchmark circuits under TSMC 22nm process, the proposed framework achieves significant correlation and accuracy improvement with an average of 0.9219 in terms of R2 score and 2.12% of mean absolute percentage error (MAPE) as well as an average runtime acceleration of$645\times $compared with traditional design flow on testing designs. With the timing optimization guidance, significant worst negative slack (WNS) and total negative slack (TNS) improvement are achieved compared with traditional flow after placement and routing, respectively, without noticeable area, power, wire length, and the number of design rule check (DRC) violations increase.
```

#### Research fact 2

The paper proposed a prerouting path-delay prediction framework using a Transformer network and a residual model, extracting placement-stage timing and physical information as sequential features and modeling path-delay residuals to calibrate the difference between prerouting and postrouting delay.

> In this paper, an efficient and accurate pre-routing path delay prediction framework is proposed by employing transformer network and residual model, where the timing and physical information at placement stage is extracted as sequence features while the residual of path delay is modeled to calibrate the mismatch between the pre- and post-routing path delay.

[Paper Pre-Routing Path Delay Estimation Based on Transformer and Residual Framework](https://doi.org/10.1109/asp-dac52403.2022.9712484)

**Title and abstract passage supplied on that run**

```text
Pre-Routing Path Delay Estimation Based on Transformer and Residual Framework
Timing estimation prior to routing is of vital importance for optimization at placement stage and timing closure. Existing wire- or net-oriented learning-based methods limits the accuracy and efficiency of prediction due to the neglect of the delay correlation along path and computational complexity for delay accumulation. In this paper, an efficient and accurate pre-routing path delay prediction framework is proposed by employing transformer network and residual model, where the timing and physical information at placement stage is extracted as sequence features while the residual of path delay is modeled to calibrate the mismatch between the pre- and post-routing path delay. Experimental results demonstrate that with the proposed framework, the prediction error of post-routing path delay is less than 1.68% and 3.12% for seen and unseen circuits in terms of rRMSE, which is reduced by 2.3~5.0 times compared with exiting learning-based method for pre-routing prediction. Moreover, this framework produces at least three orders of magnitude speedup compared with the traditional design flow, which is promising to guide circuit optimization with satisfying prediction accuracy prior to time-consuming routing and timing analysis.
```

#### Collaboration rationale

If a domain language model is to be applied to prerouting timing prediction, this candidate's experience in timing prediction and multimodal feature extraction could offer a complementary method. However, the task is prediction rather than layout generation; integration with the chip-design flow needs validation.

#### Items requiring confirmation

Confirm whether the candidate has usable real design data, technology-library licenses, conditions for validating executable design flows, and current willingness to collaborate.

- K001.status ｜ Your judgment (R2 reasonable conditional suggestion; R1 direction plausible but needs local revision; R0 insufficient basis or clearly unsuitable; RU unable to judge)：________

- K001.note ｜ Basis for judgment or information needed：________

- K001.flag_Demand drift ｜ Demand drift：________

- K001.flag_Personal attribution ｜ Personal attribution：________

- K001.flag_Unsupported negative claim ｜ Unsupported negative claim：________

- K001.flag_Transfer conditions ｜ Transfer conditions：________

- K001.flag_Resource or willingness commitment ｜ Resource or willingness commitment：________

### K015 Candidate P009

#### Research fact 1

The paper proposed ChatChisel, a language-based agile hardware-design workflow using four LLM-based modules for decomposing, generating, correcting and composing hardware designs.

> We introduce ChatChisel, the first language-based agile hardware design workflow that generates Chisel from language specifications. ChatChisel utilizes four LLM-based modules for decomposing, generating, error-correcting, and composing hardware designs.

[Paper ChatChisel: Enabling Agile Hardware Design with Large Language Models](https://doi.org/10.1109/iseda62518.2024.10618053)

**Title and abstract passage supplied on that run**

```text
ChatChisel: Enabling Agile Hardware Design with Large Language Models
With the increasing complexity of integrated circuits, agile hardware design methodologies are crucial. Modern HDLs like Chisel enhance design quality, but manual implementations remain error-prone and time-consuming. Large language models (LLMs) offer potential for design automation through natural language but face challenges in generating large circuits using Verilog. We evaluate LLM capabilities for Chisel and Verilog generation, demonstrating superior Chisel generation ability. We introduce ChatChisel, the first language-based agile hardware design workflow that generates Chisel from language specifications. ChatChisel utilizes four LLM-based modules for decomposing, generating, error-correcting, and composing hardware designs. Techniques like LLM collaboration and RAG enhance ChatChisel's performance. Using GPT-3.5-turbo, we implemented an RV32I RISC-V CPU with 5-stage pipeline and dynamic branch prediction. We also validate our approach with extensive evaluations. Our experimental results reveal that ChatChisel can outperform LLM-based hardware design with Verilog by an average of 31.86%, implying a significant design capability enhancement and design process acceleration with ChatChisel.
```

#### Research fact 2

The paper's MMCircuitEval benchmark contains 3,614 question–answer pairs covering key EDA stages from front-end to back-end design for digital and analog circuits.

> MMCircuitEval comprises 3614 meticulously curated question-answer (QA) pairs spanning digital and analog circuits across critical EDA stages—ranging from general knowledge and specifications to front-end and back-end design.

[Paper MMCircuitEval: A Comprehensive Multimodal Circuit-Focused Benchmark for Evaluating LLMs](https://doi.org/10.1109/iccad66269.2025.11240653)

**Title and abstract passage supplied on that run**

```text
MMCircuitEval: A Comprehensive Multimodal Circuit-Focused Benchmark for Evaluating LLMs
The emergence of multimodal large language models (MLLMs) presents promising opportunities for automation and enhancement in Electronic Design Automation (EDA). However, comprehensively evaluating these models in circuit design remains challenging due to the narrow scope of existing benchmarks. To bridge this gap, we introduce MMCircuitEval, the first multimodal benchmark specifically designed to assess MLLM performance comprehensively across diverse EDA tasks. MMCircuitEval comprises 3614 meticulously curated question-answer (QA) pairs spanning digital and analog circuits across critical EDA stages—ranging from general knowledge and specifications to front-end and back-end design. Derived from textbooks, technical question banks, datasheets, and real-world documentation, each QA pair undergoes rigorous expert review for accuracy and relevance. Our benchmark uniquely categorizes questions by design stage, circuit type, tested abilities (knowledge, comprehension, reasoning, computation), and difficulty level, enabling detailed analysis of model capabilities and limitations. Extensive evaluations reveal significant performance gaps among existing LLMs, particularly in back-end design and complex computations, highlighting the critical need for targeted training datasets and modeling approaches. MMCircuitEval provides a foundational resource for advancing MLLMs in EDA, facilitating their integration into real-world circuit design workflows. Our benchmark is available at https://github.com/cure-lab/MMCircuitEval.
```

#### Collaboration rationale

If a domain language model is to be applied to chip design, this candidate's LLM hardware-generation workflow and benchmark covering front-end and back-end design could offer ideas for task decomposition and evaluation. However, neither involves timing, physical design or validation of executable design flows.

#### Items requiring confirmation

Establish whether the candidate has knowledge of timing/physical-design tasks, usable real design data and technology-library licenses, and can participate in validating executable design flows.

- K015.status ｜ Your judgment (R2 reasonable conditional suggestion; R1 direction plausible but needs local revision; R0 insufficient basis or clearly unsuitable; RU unable to judge)：________

- K015.note ｜ Basis for judgment or information needed：________

- K015.flag_Demand drift ｜ Demand drift：________

- K015.flag_Personal attribution ｜ Personal attribution：________

- K015.flag_Unsupported negative claim ｜ Unsupported negative claim：________

- K015.flag_Transfer conditions ｜ Transfer conditions：________

- K015.flag_Resource or willingness commitment ｜ Resource or willingness commitment：________

### K017 Candidate P003

#### Research fact 1

The paper proposed a multimodal model combining power-delivery-network, layout and netlist data, incorporating auxiliary and contrastive learning to capture differences among power-delivery networks, and experimented on open-source designs.

> To address this challenge, we propose a multimodal model that integrates PDN, layout, and netlist data. Additionally, we incorporate auxiliary and contrastive learning techniques to capture the differences across various PDNs. Extensive experiments on open-source designs demonstrate the superior performance of our model.

[Paper Pre-Routing Timing Estimation Considering Power Delivery Network](https://doi.org/10.1109/iseda65950.2025.11100758)

**Title and abstract passage supplied on that run**

```text
Pre-Routing Timing Estimation Considering Power Delivery Network
In recent years, the demand for fast and accurate pre-routing timing prediction is increasing. However, existing machine learning (ML)-based methods for predicting pre-routing timing often overlook the impact of power delivery networks (PDNs), which are critical to IR drop and routing congestion, limiting the effectiveness of these approaches in real-world circuit designs. To address this challenge, we propose a multimodal model that integrates PDN, layout, and netlist data. Additionally, we incorporate auxiliary and contrastive learning techniques to capture the differences across various PDNs. Extensive experiments on open-source designs demonstrate the superior performance of our model.
```

#### Research fact 2

The paper proposed a learning-driven, physically aware gate-sizing framework, constructing a multimodal gate-sizing-aware timing model by jointly learning timing information from multiple timing paths and physical information from multiscale layouts.

> In this work, we propose a learning-driven physically aware gate sizing framework to optimize timing performance on large-scale circuits efficiently. In our gradient descent optimization-based work, for obtaining accurate gradients, a multimodal gate sizing-aware timing model is achieved via learning timing information on multiple timing paths and physical information on multiple-scaled layouts jointly.

[Paper Learning-Driven Physically Aware Large-Scale Circuit Gate Sizing](https://doi.org/10.1109/tcad.2024.3488577)

**Title and abstract passage supplied on that run**

```text
Learning-Driven Physically Aware Large-Scale Circuit Gate Sizing
Gate sizing plays an important role in timing optimization after physical design. Existing machine learning-based gate sizing works cannot optimize timing on multiple timing paths simultaneously and neglect the physical constraint on layouts. They cause suboptimal sizing solutions and low-efficiency issues when compared with commercial gate sizing tools. In this work, we propose a learning-driven physically aware gate sizing framework to optimize timing performance on large-scale circuits efficiently. In our gradient descent optimization-based work, for obtaining accurate gradients, a multimodal gate sizing-aware timing model is achieved via learning timing information on multiple timing paths and physical information on multiple-scaled layouts jointly. Then, gradient generation based on the sizing-oriented estimator and adaptive back-propagation are developed to update gate sizes. Our results demonstrate that our work achieves higher-timing performance improvements in a faster way compared with the commercial gate sizing tool.
```

#### Collaboration rationale

If a domain language model is to be applied to timing and physical-design tasks, this candidate's experience in multimodal modeling and physically aware optimization could be complementary. However, the data are open-source designs and the tasks are prediction and optimization; compatibility with real design flows needs validation.

#### Items requiring confirmation

Confirm whether the candidate has usable real design data, technology-library licenses, conditions for validating executable design flows, and current willingness to collaborate.

- K017.status ｜ Your judgment (R2 reasonable conditional suggestion; R1 direction plausible but needs local revision; R0 insufficient basis or clearly unsuitable; RU unable to judge)：________

- K017.note ｜ Basis for judgment or information needed：________

- K017.flag_Demand drift ｜ Demand drift：________

- K017.flag_Personal attribution ｜ Personal attribution：________

- K017.flag_Unsupported negative claim ｜ Unsupported negative claim：________

- K017.flag_Transfer conditions ｜ Transfer conditions：________

- K017.flag_Resource or willingness commitment ｜ Resource or willingness commitment：________

### K011 Candidate P004

#### Research fact 1

The study validated the proposed preplacement timing-prediction and optimization framework using ISCAS'89, OpenCores and Gaisler benchmark circuits in TSMC 22 nm technology.

> The proposed pre-placement timing prediction and optimization framework was validated under TSMC 22nm process with the ISCAS’89, OpenCores, and Gaisler benchmark circuits.

[Paper Physical-Aware Multicorner Timing Prediction for Pre-Placement Optimization Using BiLSTM and GNN Networks](https://doi.org/10.1109/tcad.2025.3646591)

**Title and abstract passage supplied on that run**

```text
Physical-Aware Multicorner Timing Prediction for Pre-Placement Optimization Using BiLSTM and GNN Networks
The timing inpredictability at early design stage poses significant challenge to design convergence of integrated circuits, especially under multiple PVT corners. Prior works have concentrated exclusively on research of timing correlation and the related impact to circuit design across multiple design stages or corners, without addressing the influence of both on the final prediction accurately and efficiently. In this work, a physical aware timing prediction framework for multiple corners is proposed for pre-placement prediction and optimization by employing the bidirectional LSTM network and MLP network to learn the correlation from the sequence features and global features at logic synthesis stage, in which a GNN-based model is utilized to estimate the HPWL as physical feature, addressing the timing prediction challenge suffering from physical information absence. Besides, a corner selection mechanism is introduced to reduce the post-synthesis feature extraction overhead from multiple corners. The proposed pre-placement timing prediction and optimization framework was validated under TSMC 22nm process with the ISCAS’89, OpenCores, and Gaisler benchmark circuits. Significant prediction accuracy improvement is achieved to estimate the post-placement path delay for 12 PVT corners by post-synthesis timing analysis results under 5 corners with an average rRMSE of 8.75% for unseen designs, demonstrating a 19×∼53× runtime speedup. Significant placement quality improvement is achieved in terms of 25.96% ADP reduction and 20.52% PDP reduction in average compared to traditional design flow.
```

#### Research fact 2

The work experimented on ISCAS'89 benchmark circuits in TSMC 22 nm technology; the proposed framework achieved average critical-path prediction F1 scores of 95.0% and 93.6% on seen and unseen circuits, respectively.

> Experimental results demonstrate that with the proposed framework, the average prediction accuracy of critical paths achieves 95.0% and 93.6% for seen and unseen circuits in terms of F1-score for ISCAS’89 benchmark circuits under TSMC 22nm process

[Paper Critical Paths Prediction under Multiple Corners Based on BiLSTM Network](https://doi.org/10.1109/dac56929.2023.10247984)

**Title and abstract passage supplied on that run**

```text
Critical Paths Prediction under Multiple Corners Based on BiLSTM Network
Critical path generation poses significant challenge to integrated circuit (IC) design flow in terms of huge computational complexity and crucial impact to circuit optimization, whose early prediction is of vital importance for accelerating the design closure, especially under multiple process-voltage-temperature (PVT) corners. In this work, a post-routing critical path prediction framework is proposed based on Bidirectional Long Short-Term Memory (BiLSTM) network and Multi-Layer Perceptron (MLP) network to learn from the sequential features and global features at logic synthesis stage, which are extracted from the timing and physical information of cell sequences and operation conditions for circuit respectively. Experimental results demonstrate that with the proposed framework, the average prediction accuracy of critical paths achieves 95.0% and 93.6% for seen and unseen circuits in terms of F1-score for ISCAS’89 benchmark circuits under TSMC 22nm process, demonstrating an increase of 10.8% and 13.9% compared with existing learning-based critical paths prediction method.
```

#### Collaboration rationale

If a domain language model is to be applied to timing and preplacement prediction, this candidate's experience in timing prediction and physically aware modeling could be complementary. However, validation used benchmark circuits and a specific technology; transfer to real design data and executable flows needs confirmation.

#### Items requiring confirmation

Establish whether the candidate can obtain and authorize use of real design data, what technology libraries and EDA flows are currently available, and whether they are willing to participate in joint validation.

- K011.status ｜ Your judgment (R2 reasonable conditional suggestion; R1 direction plausible but needs local revision; R0 insufficient basis or clearly unsuitable; RU unable to judge)：________

- K011.note ｜ Basis for judgment or information needed：________

- K011.flag_Demand drift ｜ Demand drift：________

- K011.flag_Personal attribution ｜ Personal attribution：________

- K011.flag_Unsupported negative claim ｜ Unsupported negative claim：________

- K011.flag_Transfer conditions ｜ Transfer conditions：________

- K011.flag_Resource or willingness commitment ｜ Resource or willingness commitment：________

### K012 Candidate P012

#### Research fact 1

The paper advocates developing multimodal circuit-representation learning to provide comprehensive understanding by harmonizing and extracting insights from data sources including functional specifications, RTL designs, circuit netlists and physical layouts.

> Pivotal to this vision is the development of a multimodal circuit representation learning technique, poised to provide a comprehensive understanding by harmonizing and extracting insights from varied data sources, such as functional specifications, register-transfer level (RTL) designs, circuit netlists, and physical layouts.

[Paper Large circuit models: opportunities and challenges](https://doi.org/10.1007/s11432-024-4155-7)

**Title and abstract passage supplied on that run**

```text
Large circuit models: opportunities and challenges
Abstract Within the electronic design automation (EDA) domain, artificial intelligence (AI)-driven solutions have emerged as formidable tools, yet they typically augment rather than redefine existing methodologies. These solutions often repurpose deep learning models from other domains, such as vision, text, and graph analytics, applying them to circuit design without tailoring to the unique complexities of electronic circuits. Such an “AI4EDA” approach falls short of achieving a holistic design synthesis and understanding, overlooking the intricate interplay of electrical, logical, and physical facets of circuit data. This study argues for a paradigm shift from AI4EDA towards AI-rooted EDA from the ground up, integrating AI at the core of the design process. Pivotal to this vision is the development of a multimodal circuit representation learning technique, poised to provide a comprehensive understanding by harmonizing and extracting insights from varied data sources, such as functional specifications, register-transfer level (RTL) designs, circuit netlists, and physical layouts. We champion the creation of large circuit models (LCMs) that are inherently multimodal, crafted to decode and express the rich semantics and structures of circuit data, thus fostering more resilient, efficient, and inventive design methodologies. Embracing this AI-rooted philosophy, we foresee a trajectory that transcends the current innovation plateau in EDA, igniting a profound “shift-left” in electronic design methodology. The envisioned advancements herald not just an evolution of existing EDA tools but a revolution, giving rise to novel instruments of design-tools that promise to radically enhance design productivity and inaugurate a new epoch where the optimization of circuit performance, power, and area (PPA) is achieved not incrementally, but through leaps that redefine the benchmarks of electronic systems’ capabilities.
```

#### Research fact 2

The paper's ForgeEDA dataset includes multiple circuit representations: RTL code, post-mapping netlists, and-inverter graphs and placed netlists.

> ForgeEDA includes diverse circuit representations such as Register Transfer Level (RTL) code, Post-mapping (PM) netlists, And-Inverter Graphs (AIGs), and placed netlists, enabling comprehensive analysis and development.

[Paper ForgeEDA: A Comprehensive Multimodal Dataset for Advancing EDA](https://doi.org/10.1109/iseda65950.2025.11101194)

**Title and abstract passage supplied on that run**

```text
ForgeEDA: A Comprehensive Multimodal Dataset for Advancing EDA
We introduce ForgeEDA, an open-source comprehensive circuit dataset across various categories. ForgeEDA includes diverse circuit representations such as Register Transfer Level (RTL) code, Post-mapping (PM) netlists, And-Inverter Graphs (AIGs), and placed netlists, enabling comprehensive analysis and development. We demonstrate ForgeEDA’s utility by benchmarking state-of-the-art EDA algorithms on critical tasks such as Power, Performance, and Area (PPA) optimization, highlighting its ability to expose performance gaps and drive advancements. Additionally, ForgeEDA’s scale and diversity facilitate the training of AI models for EDA tasks, demonstrating its potential to improve model performance and generalization. By addressing limitations in existing datasets, ForgeEDA aims to catalyze breakthroughs in modern IC design and support the next generation of innovations in EDA.
```

#### Collaboration rationale

If a domain language model is to be applied to chip design, this candidate's advocacy of multimodal circuit-representation learning and an open dataset containing placed netlists could provide data-representation and layout-related task leads. However, the papers concern a review and dataset construction, and do not validate an executable design flow.

#### Items requiring confirmation

Establish whether the candidate has knowledge of timing/physical-design tasks, the dataset licensing conditions and availability of real design data, and the ability to participate in validating executable design flows.

- K012.status ｜ Your judgment (R2 reasonable conditional suggestion; R1 direction plausible but needs local revision; R0 insufficient basis or clearly unsuitable; RU unable to judge)：________

- K012.note ｜ Basis for judgment or information needed：________

- K012.flag_Demand drift ｜ Demand drift：________

- K012.flag_Personal attribution ｜ Personal attribution：________

- K012.flag_Unsupported negative claim ｜ Unsupported negative claim：________

- K012.flag_Transfer conditions ｜ Transfer conditions：________

- K012.flag_Resource or willingness commitment ｜ Resource or willingness commitment：________

## Submission attestation

- meta.attestation ｜ I have completed the above judgments and have truthfully declared my working method and any prior exposure：________

Click “Check and export results” at the top of the page. The downloaded filename contains the packet ID and “completed”; do not change its fields or identifiers.