from dataclasses import dataclass

DOMAIN = "solvis_control"

CONF_NAME = "name"
CONF_HOST = "host"
CONF_PORT = "port"

DATA_COORDINATOR = "coordinator"
MANUFACTURER = "Solvis"


@dataclass(frozen=True)
class ModbusFieldConfig:
    name: str
    address: int
    unit: str
    device_class: str
    state_class: str
    multiplier: float = 0.1
    # 1 = INPUT, 2 = HOLDING
    register: int = 1
    negative: bool = False
    absolut_value: bool = False
    entity_category: str = None
    enabled_by_default: bool = True
    edit: bool = False
    data: tuple = None


PORT = 502

# Order and naming see: https://solvis-files.s3.eu-central-1.amazonaws.com/downloads-fk/regelung/sc-3/SC-3_ModBus_Schnittstellenbeschreibung.pdf
REGISTERS = [
    ModbusFieldConfig(  # ZirkulationBetriebsart
        name="zirkulation_betriebsart",
        address=2049,
        unit="",
        device_class=None,
        state_class=None,
        multiplier=1,
        # data=("0", "1", "2", "3"),
    ),
    ModbusFieldConfig(  # VersionSC2
        name="version_sc3",
        address=32770,
        unit="",
        device_class=None,
        state_class=None,
        multiplier=1,
        entity_category="diagnostic",
    ),
    ModbusFieldConfig(  # VersionNBG
        name="version_nbg",
        address=32771,
        unit="",
        device_class=None,
        state_class=None,
        multiplier=1,
        entity_category="diagnostic",
    ),
    
    ModbusFieldConfig( # tank_layer4_water_temp
        name="temp_s1",
        address=33024,
        unit="°C",
        device_class="temperature",
        state_class="measurement",
    ),
    ModbusFieldConfig( # domestic_water_temp
        name="temp_s2",
        address=33025,
        unit="°C",
        device_class="temperature",
        state_class="measurement",
    ),
    ModbusFieldConfig( # tank_layer1_water_temp
        name="temp_s3",
        address=33026,
        unit="°C",
        device_class="temperature",
        state_class="measurement",
    ),
    ModbusFieldConfig( # tank_layer3_water_temp
        name="temp_s4",
        address=33027,
        unit="°C",
        device_class="temperature",
        state_class="measurement",
    ),
    ModbusFieldConfig( # solar_heat_exchanger_out_temp
        name="temp_s5",
        address=33028,
        unit="°C",
        device_class="temperature",
        state_class="measurement",
        enabled_by_default=False,
    ),
    ModbusFieldConfig( # solar_heat_exchanger_in_temp
        name="temp_s6",
        address=33029,
        unit="°C",
        device_class="temperature",
        state_class="measurement",
        enabled_by_default=False,
    ),
    ModbusFieldConfig( # solar_water_temp
        name="temp_s7",
        address=33030,
        unit="°C",
        device_class="temperature",
        state_class="measurement",
        enabled_by_default=False,
    ),
    ModbusFieldConfig( # solar_collector_temp_1
        name="temp_s8",
        address=33031,
        unit="°C",
        device_class="temperature",
        state_class="measurement",
    ),
    ModbusFieldConfig( # tank_layer2_water_temp
        name="temp_s9",
        address=33032,
        unit="°C",
        device_class="temperature",
        state_class="measurement",
        negative=True,
        absolut_value=True,
    ),
    ModbusFieldConfig( # outdoor_air_temp
        name="temp_s10",
        address=33033,
        unit="°C",
        device_class="temperature",
        state_class="measurement",
    ),
    ModbusFieldConfig( # circulation_return_temp
        name="temp_s11",
        address=33034,
        unit="°C",
        device_class="temperature",
        state_class="measurement",
        multiplier=0.1,
        enabled_by_default=False,
    ),
    ModbusFieldConfig( 
        name="temp_s12",
        address=33035,
        unit="°C",
        device_class="temperature",
        state_class="measurement",
        enabled_by_default=False,
    ),    
    ModbusFieldConfig(
        name="temp_s13",
        address=33036,
        unit="°C",
        device_class="temperature",
        state_class="measurement",
        enabled_by_default=False,
    ),
    ModbusFieldConfig(
        name="temp_s14",
        address=33037,
        unit="°C",
        device_class="temperature",
        state_class="measurement",
        enabled_by_default=False,
    ),
    ModbusFieldConfig(# cold_water_temp, 10°C if no sensor is connected
        name="temp_s15",
        address=33038,
        unit="°C",
        device_class="temperature",
        state_class="measurement",
    ),
    ModbusFieldConfig( # solar_collector_temp_2 (only for east-west system)
        name="temp_s16",
        address=33039,
        unit="°C",
        device_class="temperature",
        state_class="measurement",
        enabled_by_default=False,
    ),

    ModbusFieldConfig( # solar_water_flow
        name="volumenstrom_s17",
        address=33040,
        unit="l/min",
        device_class="speed",
        state_class="measurement",
        enabled_by_default=False,
    ),
    ModbusFieldConfig(  # domestic_water_flow
        name="volumenstrom_s18",
        address=33041,
        unit="l/min",
        device_class="speed",
        state_class="measurement",
    ),
    
    ModbusFieldConfig( 
        name="digin_stoerungen",
        address=33045,
        unit="",
        device_class=None,
        state_class=None,
        multiplier=1,
        entity_category="diagnostic",
    ),
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        ModbusFieldConfig(  # HKR1 Absenktemperatur Nacht
        name="hkr1_absenktemperatur_nacht",
        address=2821,
        unit="°C",
        device_class="temperature",
        state_class="measurement",
        register=2,
        multiplier=1,
        edit=True,
        data=(5, 75),
    ), 
    
    
    
    ### General ###
    ModbusFieldConfig(  # Brennerleistung
        name="gas_power",
        address=33539,
        unit="kW",
        device_class="power",
        state_class="measurement",
    ),
    ModbusFieldConfig(  # Laufzeit Brenner
        name="runtime_gasburner",
        address=33536,
        unit="h",
        device_class="time",
        state_class="measurement",
        entity_category="diagnostic",
    ),
    ModbusFieldConfig(  # Brennerstarts
        name="number_gas_burner_start",
        address=33537,
        unit="",
        device_class="",
        state_class="measurement",
        negative=True,
        multiplier=1,
        entity_category="diagnostic",
        absolut_value=True,
    ),

   


    ModbusFieldConfig(  # HKR1 Solltemperatur Tag
        name="hkr1_solltemperatur_tag",
        address=2820,
        unit="°C",
        device_class="temperature",
        state_class="measurement",
        register=2,
        multiplier=1,
        edit=True,
        data=(5, 75),
    ),
    ModbusFieldConfig(  # HKR1 Betriebsart
        name="hkr1_betriebsart",
        address=2818,
        unit="",
        device_class=None,
        state_class=None,
        register=2,
        multiplier=1,
        data=("2", "3", "4", "5", "6", "7"),
    ),
    ModbusFieldConfig(  # Raumtemperatur_HKR1
        name="raumtemperatur_hkr1",
        address=34304,
        unit="°C",
        device_class="temperature",
        state_class="measurement",
        register=2,
        edit=True,
        data=(0, 40),
    ),
    
    ### Brauchwasser ###
    ModbusFieldConfig(  # WW Solltemperatur
        name="ww_solltemperatur",
        address=2305,
        unit="°C",
        device_class="temperature",
        state_class="measurement",
        register=2,
        multiplier=1,
        edit=True,
        data=(10, 65),
    ),
    
    

    ### Weitere ###
    ModbusFieldConfig(  # Ionisationsstrom
        name="ionisation_voltage",
        address=33540,
        unit="mV",
        device_class="voltage",
        state_class="measurement",
    ),
    ModbusFieldConfig(  # A01.Pumpe Zirkulation
        name="a01_pumpe_zirkulation",
        address=33280,
        unit="V",
        device_class="voltage",
        state_class="measurement",
    ),
    ModbusFieldConfig(  # A02.Pumpe Warmwasser
        name="a02_pumpe_warmwasser",
        address=33281,
        unit="V",
        device_class="voltage",
        state_class="measurement",
    ),
    ModbusFieldConfig(  # A03.Pumpe HK1
        name="a03_pumpe_hk1",
        address=33282,
        unit="V",
        device_class="voltage",
        state_class="measurement",
    ),
    ModbusFieldConfig(  # A05.Pumpe Zirkulation
        name="a05_pumpe_zirkulation",
        address=33284,
        unit="V",
        device_class="voltage",
        state_class="measurement",
    ),
    ModbusFieldConfig(  # A12.Brennerstatus
        name="a12_brennerstatus",
        address=33291,
        unit="V",
        device_class="voltage",
        state_class="measurement",
    ),
    ModbusFieldConfig(  # WW Nachheizung 2322
        name="ww_nachheizung_2322",
        address=2322,
        unit="V",
        device_class="voltage",
        state_class="measurement",
        register=2,
    ),
]
