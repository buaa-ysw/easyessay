from crewai import Task
from textwrap import dedent

class EssayTasks:    
    def abstract_writing_task(self, agent, topic, name):
        return Task(
            description=dedent(f"""
                Write an abstract for the essay on the topic "{topic}" and the name "{name}".
                The abstract should provide a concise summary of the key points, methodology, main findings, and conclusions of the essay.
                """),
            expected_output=dedent("""
                A well-written abstract that effectively summarizes the key aspects of the essay's topic.
                [Here is an example]
                -------------------------
                Abstract:
                \nUnmanned aerial vehicles (UAVs) have attracted a lot of attention for various applications such as service delivery, pollution mitigation, farming, and rescue operations over the past few years.
                However, the short duration of battery and the inconvenience of changing it is always a problem.
                Basically, small UAVs can only carry very limited payloads otherwise the battery will be drained more frequently.
                This project presents an automatic and high-efficient wireless power transfer (WPT) to supply a 3D printed UAV.
                A UAV has been 3D printed with wireless power transfer kit implemented to charge 3S 1500 mAh Li-Po battery with up to 1000 mAh automatically once it is landed, without manual operation.
                24V DC is supplied to the transmitting side of WPT with the operating frequency at 180kHz and once the battery is fully charged, the charging process will also stop automatically.
                -------------------------
                """),
            agent=agent
        )
        
    def introduction_writing_task(self, agent, topic, name, context):
        return Task(
            description=dedent(f"""
                Write an introduction for the essay on the topic "{topic}" and the name "{name}".
                The introduction should set the stage for the essay, providing necessary context, background information, and an overview of what readers can expect.
                [!! What you write must be logically and content-wise consistent with the ABSTRACT !!]
                """),
            expected_output=dedent("""
                A well-written introduction that effectively introduces the topic and outlines the structure of the essay.
                [Here is an example]
                -------------------------
                Introduction
                \nUnmanned aerial vehicles (UAVs) plays increasing significance in modern life, with the ability to execute multiple tasks with reliable performance such as surveillance, inspection, filming and delivery.
                The UAVs can be equipped with many payloads such as a high-resolution camera, infrared camera, sensors, etc., or with objects to deliver.
                In general, these commercially available systems are powered by a high energy density lithium battery that permits a flight time of about 20–40 min.
                However, limited battery power obviously restrains UAVs from execute the tasks continuously.
                Most UAV batteries are not durable due to many factors.
                Battery technology nowadays has many drawbacks including price, size, weight, charging speed and low energy density.
                For instance, large batteries are too heavy for a UAV to keep balance or load.
                UAV with many equipment such as camera will increase the weight, thus increase the power consumption, leading to short battery duration.
                In this case, users have to charge their UAVs or change the batteries.
                \nTo deal with the battery problem, many researchers has made developments in two mainly ways to provide a fully charged battery to UAVs – replacing the battery or recharging it.
                Wireless Power Transfer [1]-[7] for UAV Systems Application will reduce the need for users to swap batteries or to connect a power cable, negating the need to return to a single point when battery is drained or any manual operation (Fig. 1).
                WPT technology permits a very efficient and reliable power transmission between the ground base and the UAV.
                Also, since either the replacing batteries nor exposing the charging contacts to outside environment are required, the UAV can be completely sealed, allowing it to operate in harsh environments.
                This will enable UAVs to travel further from station and stay in the air longer.
                \nSome researchers also aim at expanding the practicality of WPT technology by increasing transfer power and efficiency [8], by keeping the driving frequency consistent with inherent resonance frequency of LC resonant circuit may improve the behaviour with transmitted power up to 50W, more than 60 percent efficiency at the distance of 1 meter.
                The state-of-the-art research. is also enhancing the WPT with newly-developed components like wide band-gap transistor diodes or recently discovered inverters is tolerant to load variations and have inherent voltage or current regulation features enable an WPT system to operate effectively.
                \nTo cope with battery problem, Wireless Power Transfer Technology is utilized.
                Here, a novel angle is proposed to improve the battery duration and efficiency by utilizing WPT technology aiming at becoming less sensitive to the misalignment of the coils with 3D printing technology, in addition to reduce the complexity of fabrication and total weight of UAV.
                The proposed solution consists of a ground transmitting coil module with multiple receiving on-board coils to charge 3S Li-Po battery and a self-designed pad with extended support for secondary coils with 3D printing technology.
                The theories of WPT, the reason why 3D printing is better or why I would like to transfer power wirelessly to UAV and method of design and fabrication will now be described.
                -------------------------
                """),
            agent=agent,
            context=context
        )
        
    def system_composition_writing_task(self, agent, topic, name, context):
        return Task(
            description=dedent(f"""
                Write a system composition for the essay on the topic "{topic}" and the name "{name}".
                The system composition should provide an overview of the components, structure, and interactions within the system or project.
                [!! What you write must be logically and content-wise consistent with the ABSTRACT and the INRTODUCTION !!]
                """),
            expected_output=dedent("""
                A well-written system composition that effectively outlines the key components and their relationships within the project.
                [Here is an example]
                -------------------------
                System Composition
                \nWireless power transfer module XKT-801 (Figure 3) is utilized to compose the WPT system, which requires 24V DC input to the transmitting coil module.
                Within the chip of primary coil module has a inverter to convert the DC signal to AC signal for inductor to generate electromagnetic field to transmit power.
                At secondary coil side, AC signal needs to convert back to DC for the battery.
                The embedded rectifier is used to do this job.
                \nThe output voltage from the Wireless Power Transfer System cannot charge the battery directly.
                A balance charger is needed to ensure the several-cells-in-series Li-Po battery can be discharged and charged properly.
                \nThe basic principle of balance charging is to detect the difference between the voltage of different cells and charge them separately with either large current for low-voltage cells or small current for high-voltage cells.
                In this case, TP4056 is selected as the battery charging module.
                \nBecause we are using the 3s Li-po 1500mAh battery, which is composed of three cells in series.
                Fig. 6(a) shows the internal connection of the battery.
                As a result, three TP4056 in series is needed to balance charge this battery.
                Also, the charging current is changed from the default value of 1000mAh to 520mAh by changing R3 with a resistor of 2.3kΩ.
                This is because the greater normal charging current does not bring better charging result or may even do harm to the Li-Po battery.
                \nThe required input of the TP4056 module is 5V DC, which is another important reason why this module is chosen--- the output from the receiving coil module of Wireless Power Transfer System is exactly 5V within the operating distance of 12cm, according to Table 1.
                As shown in Fig. 6(b), three receiving coils are utilized to provide 5V DC input for three TP4056 separately.
                This configuration will balance charge three cells of the 3S Li-Po battery.
                After several experiments, the TP4056 will monitor the voltage of cells and change the charging current accordingly.
                \nIn a previous work [12], the on-board coil has been placed on the landing skid.
                Such a solution permits an enhancement of the system performance due to the increase of the coupling factor between the coils by reducing the vertical air gap between the transmitting and receiving coils.
                However, it requires high accuracy of alignment.
                Its main drawback is the poor robustness to the misalignment condition because of the small dimension of the receiving coil.
                This problem maybe pretty critical as landing precision is relatively hard to control in UAV applications since it depends much on the landing algorithm or environment or landing assistance system.
                \nAdditionally, in order to ensure the proper transmission of energy and the stability of electromagnetic field, there must be no metal in the vertical space of the receiving coil, which obviously include most of the components on the UAV, like the battery, power distribution board or flight control.
                \nIn the proposed new configuration, the receiving coil is placed on an extended support from the board.
                Accurate landing is no longer necessary as long as the receiving coil is in the vertical space of the primary coil.
                This should significantly reduce the complexity of landing algorithm or stringent requirement of landing point as well as reduce the effect of metal components on power transmission.
                \n3D printing technology is utilized to build the extended support.
                3D Printing allows makers to manufacture personalized products according to an individual's needs and requirements.
                This increases the feasibility of making customized UAVs.
                Any specific part of a store-bought UAV can also be tailored to suit personal needs.
                As a WPT system is required to be mounted onto the UAV, there was a slight modification to the stl file and managed to build an extended support for the receiving coils, as shown in Fig. 7.
                In this case, there is no need to find an alternative stick, drill a hole on the board and connect them with screws.
                Obviously using 3D printing technology saves plenty of time in manufacturing.
                -------------------------
                """),
            agent=agent,
            context=context
        )
        
    def system_principle_writing_task(self, agent, topic, name, context):
        return Task(
            description=dedent(f"""
                Write system principles for the essay on the topic "{topic}" and the name "{name}".
                System principles define the fundamental rules, guidelines, and values that govern the design, development, and operation of a system or project.
                [!! What you write must be logically and content-wise consistent with the ABSTRACT, INTRODUCTION, and SYSTEM COMPOSITION !!]
                """),
            expected_output=dedent("""
                A well-defined set of system principles that reflect the project's goals, constraints, and requirements, guiding decision-making and ensuring coherence in the system design and implementation.
                """),
            agent=agent,
            context=context
        )
        
    def result_analysis_writing_task(self, agent, topic, name, context):
        return Task(
            description=dedent(f"""
                Write a result analysis for the essay on the topic "{topic}" and the name "{name}".
                Result analysis involves interpreting and explaining the findings or outcomes of a project or experiment.
                [!! What you write must be logically and content-wise consistent with the ABSTRACT, INTRODUCTION, SYSTEM COMPOSITION, and SYSTEM PRINCIPLES !!]
                """),
            expected_output=dedent("""
                A well-written result analysis that effectively interprets and explains the findings or outcomes of the project, providing valuable insights and implications.
                [Here is an example]
                -------------------------
                Result Analysis
                \nA UAV based on 3D-Printed frame is fabricated and implemented with the WPT system to test the behavior of wireless power transfer and battery charging.
                First, the UAV is manually operated, until it flies near the transmitting coil module on the ground, connected to 24V DC source.
                When the UAV approaches the transmitting coil, the LED on battery charging module showing the battery starts to be charged.
                After landing at the ground for charging, the UAV is then started again.
                When UAV leaves the operating distance of the WPT system, the LED goes blue and the battery charging is cut-off.
                \nAccording to experiments, a distance up to 12cm is within the efficient operating zone for the wireless power transfer system.
                When primary coils on the ground and the on-board receiving coils are separated beyond this distance, charging process will stop.
                When transmitter and receivers are close enough to the effective range again, charging process will start.
                It can be seen from the Fig. 8 that the Li-Po battery is connected to the battery charging module.
                The red LED shows the battery is being charged.
                From the zoom-in part of DC power source, the input power is 2.76W.
                If the voltage of cells is lower than 4.2V, battery charging module TP4056 will charge battery with set current according to Rx (Section 4.2).
                When the battery voltage is approaching the limit value of battery charging module, the LED will turn blue and charging current will turn to zero, thus cut off the charging.
                -------------------------
                """),
            agent=agent,
            context=context
        )
        
    def innovation_points_writing_task(self, agent, topic, name, context):
        return Task(
            description=dedent(f"""
                Identify and articulate innovation points for the essay on the topic "{topic}" and the name "{name}".
                Innovation points are key aspects or features that introduce novel and creative elements to a project.
                [!! What you write must be logically and content-wise consistent with the ABSTRACT, INTRODUCTION, SYSTEM COMPOSITION, SYSTEM PRINCIPLES, and RESULT ANALYSIS !!]
                """),
            expected_output=dedent("""
                A well-articulated set of innovation points that effectively highlight the novel and creative elements introduced by the project, showcasing its potential for innovation and impact.
                """),
            agent=agent,
            context=context
        )

    def market_prospect_writing_task(self, agent, topic, name, context):
        return Task(
            description=dedent(f"""
                Analyze and outline market prospects for the essay on the topic "{topic}" and the name "{name}".
                Market prospects analysis involves evaluating the potential market demand, competition, and opportunities for project innovations.
                [!! What you write must be logically and content-wise consistent with the ABSTRACT, INTRODUCTION, SYSTEM COMPOSITION, SYSTEM PRINCIPLES, RESULT ANALYSIS, and INNOVATION POINTS !!]
                """),
            expected_output=dedent("""
                A well-analyzed and outlined market prospects section that effectively evaluates the potential market demand, competition, and opportunities for project innovations, providing valuable insights for stakeholders.
                """),
            agent=agent,
            context=context
        )
        
    def conclusion_writing_task(self, agent, topic, name, context):
        return Task(
            description=dedent(f"""
                Write a conclusion for the essay on the topic "{topic}" and the name "{name}".
                The conclusion should effectively summarize the key points discussed in the essay and provide a final perspective on the topic.
                [!! What you write must be logically and content-wise consistent with the ABSTRACT, INTRODUCTION, SYSTEM COMPOSITION, SYSTEM PRINCIPLES, RESULT ANALYSIS, INNOVATION POINTS, and MARKET PROSPECTS !!]
                """),
            expected_output=dedent("""
                A well-written conclusion that effectively summarizes the key points discussed in the essay, provides a final perspective on the topic, and leaves a lasting impression on the reader.
                [Here is an example]
                -------------------------
                Conclusion
                \nIn this paper, a UAV and a Wireless Power Transfer System is fabricated and applied to it to fulfill the purpose of charging the UAV without manual operation or cable connection.
                The basic theories of WPT and analysis based on numerical methods are also introduced to make decision on components selection, designing, and utilization.
                3D printing technology has been utilized to improve the behavior the UAV while not impairing the strength of material and also reduce the complexity of fabrication, which is meaningful in mass production or individual application.
                \nThis proposed solution is also significant in providing a possibility to build an autonomous system [13]–​[17].
                It is based on WPT System on UAV application that UAV with routine mission like surveillance, monitoring or couriers can finish their job and return to charging station when battery is drained.
                After a short time of charging, UAVs can repeat the mission again, while the whole process is manual-operation-free.
                This may greatly reduce the cost of labor and more workers can put in meaningful jobs instead of connecting UAVs to power cables.
                -------------------------
                """),
            agent=agent,
            context=context
        )
        
    def bibliography_writing_task(self, agent, topic, name, context):
        return Task(
            description=dedent(f"""
                Create a bibliography for the essay on the topic "{topic}" and the name "{name}".
                The bibliography should list all the sources cited or consulted during the writing process, formatted correctly according to the specified citation style.
                [!! What you write must be logically and content-wise consistent with the ABSTRACT, INTRODUCTION, SYSTEM COMPOSITION, SYSTEM PRINCIPLES, RESULT ANALYSIS, INNOVATION POINTS, MARKET PROSPECTS, and CONCLUSION !!]
                """),
            expected_output=dedent("""
                A well-crafted bibliography that accurately documents all the sources cited or consulted during the writing process, formatted correctly according to the specified citation style.
                [Here is an example]
                -------------------------
                References
                1. G.A. Covic and J.T. Boys, "Inductive power transfer", Proc. IEEE, vol. 101, pp. 1276-1289, 2013.
                2. N. Shinohara, "Power without wires", IEEE Microw. Mag., vol. 11, pp. 64-73, 2011.
                3. T. Campi, S. Cruciani, F. Maradei and M. Feliziani, "Near Field reduction in a Wireless Power Transfer System using LCC compensation", IEEE Trans. Electromagn. Compat., vol. 59, pp. 686-694, 2017.
                4. T. Campi, S. Cruciani, V. De Santis and M. Feliziani, "EMF safety and thermal aspects in a pacemaker equipped with a wireless power transfer system working at low frequency", IEEE Trans. Microw. Theory Tech., vol. 64, pp. 375-382, 2016.
                5. A.M. Jawad, R. Nordin, S.K. Gharghan, H.M. Jawad and M. Ismail, "Opportunities and Challenges for Near-Field Wireless Power Transfer: A Review", Energies, vol. 10, pp. 1022, 2017.
                6. V. Vijayakumaran Nair and J.R. Choi, "An Efficiency Enhancement Technique for a Wireless Power Transmission System Based on a Multiple Coil Switching Technique", Energies, vol. 9, pp. 156, 2016.
                7. M. Feliziani, T. Campi, S. Cruciani, F. Maradei, U. Grasselli, M. Macellari, et al., "Robust LCC compensation in wireless power transfer with variable coupling factor due to coil misalignment", Proceedings of the 2015 IEEE 15th International Conference on Environment and Electrical Engineering (EEEIC), 10–13 June 2015.
                8. C. Zhu, K. Liu, C. Yu, R. Ma and H. Cheng, "Simulation and experimental analysis on wireless energy transfer based on magnetic resonances", Vehicle Power and Propulsion Conference, pp. 1-4, 2008, sept. 2008.
                9. Samer Aldhaher, Paul D. Mitcheson, Juan M. Arteaga, George Kkelis and David C. Yates, "Light-Weight Wireless Power Transfer for Mid-Air Charging of Drones", 2017 11th European Conference on Antennas and Propagation (EUCAP).
                -------------------------
                """),
            agent=agent,
            context=context
        )







