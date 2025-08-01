from lxml import etree


def initPrisma():
    # Initialize a new Prism XML structure with basic elements
    xml_string = '''<?xml version="1.0" encoding="UTF-8"?>
    <GraphPadPrismFile xmlns="http://graphpad.com/prism/Prism.htm" PrismXMLVersion="5.00">
        <Created>
            <OriginalVersion CreatedByProgram="GraphPad Prism" CreatedByVersion="10.5.0.774" Login="YenNomi" DateTime="2025-07-12T00:03:44+09:00"/>
        </Created>
        <InfoSequence>
            <Ref ID="Info0" Selected="1"/>
            <Ref ID="Info1"/>
        </InfoSequence>
        <Info ID="Info0">
            <Title>Project info 1</Title>
            <Notes/>
            <Constant>
                <Name>Experiment Date</Name>
                <Value>2024-09-06</Value>
            </Constant>
            <Constant>
                <Name>Experiment ID</Name>
                <Value/>
            </Constant>
            <Constant>
                <Name>Notebook ID</Name>
                <Value/>
            </Constant>
            <Constant>
                <Name>Project</Name>
                <Value/>
            </Constant>
            <Constant>
                <Name>Experimenter</Name>
                <Value/>
            </Constant>
            <Constant>
                <Name>Protocol</Name>
                <Value/>
            </Constant>
        </Info>
        <Info ID="Info1">
            <Title>Project info 1</Title>
            <Notes/>
            <Constant>
                <Name>Experiment Date</Name>
                <Value>2024-09-06</Value>
            </Constant>
            <Constant>
                <Name>Experiment ID</Name>
                <Value/>
            </Constant>
            <Constant>
                <Name>Notebook ID</Name>
                <Value/>
            </Constant>
            <Constant>
                <Name>Project</Name>
                <Value/>
            </Constant>
            <Constant>
                <Name>Experimenter</Name>
                <Value/>
            </Constant>
            <Constant>
                <Name>Protocol</Name>
                <Value/>
            </Constant>
        </Info>
        <TableSequence Selected="1">
            <Ref ID="Table0" Selected="1"/>
            <Ref ID="Table1"/>
            <Ref ID="Table2"/>
            <Ref ID="Table3"/>
        </TableSequence>
        <Table ID="Table0" XFormat="numbers" YFormat="replicates" Replicates="5" TableType="XY" EVFormat="AsteriskAfterNumber">
            <Title>in sunny place_good smell</Title>
            <RowTitlesColumn Width="39">
                <Subcolumn/>
            </RowTitlesColumn>
            <XColumn Width="161" Subcolumns="1" Decimals="0">
                <Title>Times for germination (day)</Title>
            </XColumn>
            <XAdvancedColumn Version="1" Width="161" Decimals="0" Subcolumns="1">
                <Title>Times for germination (day)</Title>
            </XAdvancedColumn>
            <YColumn Width="300" Decimals="1" Subcolumns="5">
                <Title>many fruits_normal color</Title>
            </YColumn>
            <YColumn Width="300" Decimals="1" Subcolumns="5">
                <Title>many fruits_good color</Title>
            </YColumn>
            <YColumn Width="300" Decimals="2" Subcolumns="5">
                <Title>a few fruits_normal color</Title>
            </YColumn>
            <YColumn Width="300" Decimals="1" Subcolumns="5">
                <Title>a few fruits_good color</Title>
            </YColumn>
        </Table>
        <Table ID="Table1" XFormat="numbers" YFormat="replicates" Replicates="5" TableType="XY" EVFormat="AsteriskAfterNumber">
            <Title>in sunny place or shade_good smell</Title>
            <RowTitlesColumn Width="39">
                <Subcolumn/>
            </RowTitlesColumn>
            <XColumn Width="161" Subcolumns="1" Decimals="0">
                <Title>Times for germination (day)</Title>
            </XColumn>
            <XAdvancedColumn Version="1" Width="161" Decimals="0" Subcolumns="1">
                <Title>Times for germination (day)</Title>
            </XAdvancedColumn>
            <YColumn Width="300" Decimals="1" Subcolumns="5">
                <Title>many fruits_normal color (in sunny place)</Title>
            </YColumn>
            <YColumn Width="300" Decimals="1" Subcolumns="5">
                <Title>many fruits_normal color (in shade)</Title>
            </YColumn>
            <YColumn Width="300" Decimals="1" Subcolumns="5">
                <Title>many fruits_good color (in sunny place)</Title>
            </YColumn>
            <YColumn Width="300" Decimals="1" Subcolumns="5">
                <Title>many fruits_good color (in shade)</Title>
            </YColumn>
        </Table>
        <Table ID="Table2" XFormat="numbers" YFormat="replicates" Replicates="5" TableType="XY" EVFormat="AsteriskAfterNumber">
            <Title>in sunny place or shade_good smell_many flower</Title>
            <RowTitlesColumn Width="39">
                <Subcolumn/>
            </RowTitlesColumn>
            <XColumn Width="161" Subcolumns="1" Decimals="0">
                <Title>Times for germination (day)</Title>
            </XColumn>
            <XAdvancedColumn Version="1" Width="161" Decimals="0" Subcolumns="1">
                <Title>Times for germination (day)</Title>
            </XAdvancedColumn>
            <YColumn Width="300" Decimals="1" Subcolumns="5">
                <Title>many fruits (in sunny place)</Title>
            </YColumn>
            <YColumn Width="300" Decimals="2" Subcolumns="5">
                <Title>many fruits (in shade)</Title>
            </YColumn>
            <YColumn Width="300" Decimals="2" Subcolumns="5">
                <Title>a few fruits (in sunny place)</Title>
            </YColumn>
            <YColumn Width="300" Decimals="1" Subcolumns="5">
                <Title>a few fruits (in shade)</Title>
            </YColumn>
        </Table>
        <Table ID="Table3" XFormat="numbers" YFormat="replicates" Replicates="5" TableType="XY" EVFormat="AsteriskAfterNumber">
            <Title>in sunny place_good smell_many flower</Title>
            <RowTitlesColumn Width="39">
                <Subcolumn/>
            </RowTitlesColumn>
            <SubColumnTitles OwnSet="0">
            </SubColumnTitles>
            <XColumn Width="161" Subcolumns="1" Decimals="0">
                <Title>Times for germination (day)</Title>
            </XColumn>
            <XAdvancedColumn Version="1" Width="161" Decimals="0" Subcolumns="1">
                <Title>Times for germination (day)</Title>
            </XAdvancedColumn>
            <YColumn Width="300" Decimals="1" Subcolumns="5">
                <Title>many fruits</Title>
            </YColumn>
            <YColumn Width="300" Decimals="2" Subcolumns="5">
                <Title>a few fruits</Title>
            </YColumn>
        </Table>
    </GraphPadPrismFile>
    '''
    root = etree.XML(xml_string.encode('utf-8'), parser=etree.XMLParser(remove_blank_text=True))
    tree = etree.ElementTree(root)
    tree.write('D:/2.pzfx', encoding='UTF-8', xml_declaration=True)
    return root


def initPrismaTaste():
    xml_string = '''<?xml version="1.0" encoding="UTF-8"?>
    <GraphPadPrismFile PrismXMLVersion="5.00">
        <Created>
            <OriginalVersion CreatedByProgram="GraphPad Prism" CreatedByVersion="10.1.0.264" Login="immunol" DateTime="2025-06-27T22:07:20+09:00"></OriginalVersion>
        </Created>
        <InfoSequence>
            <Ref ID="Info0" Selected="1"></Ref>
            <Ref ID="Info1"></Ref>
        </InfoSequence>
        <Info ID="Info0">
            <Title>Project info 1</Title>
            <Notes></Notes>
            <Constant>
                <Name>Experiment Date</Name>
                <Value>2024-12-23</Value>
            </Constant>
            <Constant>
                <Name>Experiment ID</Name>
                <Value></Value>
            </Constant>
            <Constant>
                <Name>Notebook ID</Name>
                <Value></Value>
            </Constant>
            <Constant>
                <Name>Project</Name>
                <Value></Value>
            </Constant>
            <Constant>
                <Name>Experimenter</Name>
                <Value></Value>
            </Constant>
            <Constant>
                <Name>Protocol</Name>
                <Value></Value>
            </Constant>
        </Info>
        <Info ID="Info1">
            <Title>Project info 1</Title>
            <Notes></Notes>
            <Constant>
                <Name>Experiment Date</Name>
                <Value>2024-12-23</Value>
            </Constant>
            <Constant>
                <Name>Experiment ID</Name>
                <Value></Value>
            </Constant>
            <Constant>
                <Name>Notebook ID</Name>
                <Value></Value>
            </Constant>
            <Constant>
                <Name>Project</Name>
                <Value></Value>
            </Constant>
            <Constant>
                <Name>Experimenter</Name>
                <Value></Value>
            </Constant>
            <Constant>
                <Name>Protocol</Name>
                <Value></Value>
            </Constant>
        </Info>
        <TableSequence>
            <Ref ID="Table0" Selected="1"></Ref>
            <Ref ID="Table1"></Ref>
            <Ref ID="Table2"></Ref>
            <Ref ID="Table3"></Ref>
            <Ref ID="Table4"></Ref>
            <Ref ID="Table8"></Ref>
            <Ref ID="Table5"></Ref>
            <Ref ID="Table6"></Ref>
            <Ref ID="Table7"></Ref>
            <Ref ID="Table9"></Ref>
            <Ref ID="Table10"></Ref>
            <Ref ID="Table11"></Ref>
            <Ref ID="Table12"></Ref>
            <Ref ID="Table13"></Ref>
        </TableSequence>
        <Table ID="Table0" XFormat="numbers" YFormat="replicates" Replicates="5" TableType="XY" EVFormat="AsteriskAfterNumber">
            <Title>in sunny place_many flower_normal or good smell_%especially tasty</Title>
            <RowTitlesColumn Width="74">
                <Subcolumn></Subcolumn>
            </RowTitlesColumn>
            <XColumn Width="40" Subcolumns="1" Decimals="0">
                <Title>Times for germination (day)</Title>
            </XColumn>
            <XAdvancedColumn Version="1" Width="40" Decimals="0" Subcolumns="1">
                <Title>Times for germination (day)</Title>
            </XAdvancedColumn>
            <YColumn Width="301" Decimals="2" Subcolumns="5">
                <Title>many fruits (normal smell)</Title>
            </YColumn>
            <YColumn Width="301" Decimals="2" Subcolumns="5">
                <Title>many fruits (good smell)</Title>
            </YColumn>
            <YColumn Width="301" Decimals="2" Subcolumns="5">
                <Title>a few fruits (normal smell)</Title>
            </YColumn>
            <YColumn Width="350" Decimals="2" Subcolumns="5">
                <Title>a few fruits (good smell)</Title>
            </YColumn>
        </Table>
        <Table ID="Table1" XFormat="numbers" YFormat="replicates" Replicates="5" TableType="XY" EVFormat="AsteriskAfterNumber">
            <Title>in sunny place or shade_many fruits_normal or good smell_%especially tasty</Title>
            <RowTitlesColumn Width="74">
                <Subcolumn></Subcolumn>
            </RowTitlesColumn>
            <XColumn Width="73" Subcolumns="1" Decimals="0">
                <Title>Times for germination (day)</Title>
            </XColumn>
            <XAdvancedColumn Version="1" Width="73" Decimals="0" Subcolumns="1">
                <Title>Times for germination (day)</Title>
            </XAdvancedColumn>
            <YColumn Width="301" Decimals="2" Subcolumns="5">
                <Title>in sunny place (normal smell)</Title>
            </YColumn>
            <YColumn Width="301" Decimals="2" Subcolumns="5">
                <Title>in sunny place  (good smell)</Title>
            </YColumn>
            <YColumn Width="301" Decimals="2" Subcolumns="5">
                <Title>in shade (normal smell)</Title>
            </YColumn>
            <YColumn Width="350" Decimals="1" Subcolumns="5">
                <Title>in shade (good smell)</Title>
            </YColumn>
        </Table>
        <Table ID="Table2" XFormat="numbers" YFormat="replicates" Replicates="5" TableType="XY" EVFormat="AsteriskAfterNumber">
            <Title>in the sunny place_fruits number and color_normal smell_%especially tasty</Title>
            <RowTitlesColumn Width="74">
                <Subcolumn></Subcolumn>
            </RowTitlesColumn>
            <XColumn Width="73" Subcolumns="1" Decimals="0">
                <Title>Times for germination (day)</Title>
            </XColumn>
            <XAdvancedColumn Version="1" Width="73" Decimals="0" Subcolumns="1">
                <Title>Times for germination (day)</Title>
            </XAdvancedColumn>
            <YColumn Width="301" Decimals="2" Subcolumns="5">
                <Title>many fruits_normal color</Title>
            </YColumn>
            <YColumn Width="301" Decimals="1" Subcolumns="5">
                <Title>many fruits_good color</Title>
            </YColumn>
            <YColumn Width="301" Decimals="2" Subcolumns="5">
                <Title>a few fruits_normal color</Title>
            </YColumn>
            <YColumn Width="350" Decimals="1" Subcolumns="5">
                <Title>a few fruits_good color</Title>
            </YColumn>
        </Table>
        <Table ID="Table3" XFormat="numbers" YFormat="replicates" Replicates="5" TableType="XY" EVFormat="AsteriskAfterNumber">
            <Title>in the sunny place_fruits number and color_good smell_%especially tasty</Title>
            <RowTitlesColumn Width="74">
                <Subcolumn></Subcolumn>
            </RowTitlesColumn>
            <XColumn Width="73" Subcolumns="1" Decimals="0">
                <Title>Times for germination (day)</Title>
            </XColumn>
            <XAdvancedColumn Version="1" Width="73" Decimals="0" Subcolumns="1">
                <Title>Times for germination (day)</Title>
            </XAdvancedColumn>
            <YColumn Width="301" Decimals="2" Subcolumns="5">
                <Title>many fruits_normal color</Title>
            </YColumn>
            <YColumn Width="301" Decimals="1" Subcolumns="5">
                <Title>many fruits_good color</Title>
            </YColumn>
            <YColumn Width="301" Decimals="2" Subcolumns="5">
                <Title>a few fruits_normal color</Title>
            </YColumn>
            <YColumn Width="350" Decimals="1" Subcolumns="5">
                <Title>a few fruits_good color</Title>
            </YColumn>
        </Table>
        <Table ID="Table4" XFormat="numbers" YFormat="replicates" Replicates="5" TableType="XY" EVFormat="AsteriskAfterNumber">
            <Title>in the sunny place or the shade_many fruits_normal smell_%especially tasty</Title>
            <RowTitlesColumn Width="74">
                <Subcolumn></Subcolumn>
            </RowTitlesColumn>
            <XColumn Width="73" Subcolumns="1" Decimals="0">
                <Title>Times for germination (day)</Title>
            </XColumn>
            <XAdvancedColumn Version="1" Width="73" Decimals="0" Subcolumns="1">
                <Title>Times for germination (day)</Title>
            </XAdvancedColumn>
            <YColumn Width="301" Decimals="2" Subcolumns="5">
                <Title>many fruits_normal color(in the sunny place)</Title>
            </YColumn>
            <YColumn Width="301" Decimals="2" Subcolumns="5">
                <Title>many fruits_normal color (in the shade)</Title>
            </YColumn>
            <YColumn Width="301" Decimals="1" Subcolumns="5">
                <Title>many fruits_good color (in the sunny place)</Title>
            </YColumn>
            <YColumn Width="350" Decimals="1" Subcolumns="5">
                <Title>many fruits_good color (in the shade)</Title>
            </YColumn>
        </Table>
        <Table ID="Table8" XFormat="numbers" YFormat="replicates" Replicates="5" TableType="XY" EVFormat="AsteriskAfterNumber">
            <Title>in the sunny place or the shade_many fruits_good smell_%especially tasty</Title>
            <RowTitlesColumn Width="74">
                <Subcolumn></Subcolumn>
            </RowTitlesColumn>
            <XColumn Width="40" Subcolumns="1" Decimals="0">
                <Title>Times for germination (day)</Title>
            </XColumn>
            <XAdvancedColumn Version="1" Width="40" Decimals="0" Subcolumns="1">
                <Title>Times for germination (day)</Title>
            </XAdvancedColumn>
            <YColumn Width="301" Decimals="2" Subcolumns="5">
                <Title>many fruits_normal color(in the sunny place)</Title>
            </YColumn>
            <YColumn Width="301" Decimals="2" Subcolumns="5">
                <Title>many fruits_normal color (in the shade)</Title>
            </YColumn>
            <YColumn Width="301" Decimals="2" Subcolumns="5">
                <Title>many fruits_good color (in the sunny place)</Title>
            </YColumn>
            <YColumn Width="350" Decimals="1" Subcolumns="5">
                <Title>many fruits_good color (in the shade)</Title>
            </YColumn>
        </Table>
        <Table ID="Table5" XFormat="numbers" YFormat="replicates" Replicates="5" TableType="XY" EVFormat="AsteriskAfterNumber">
            <Title>in the sunny place_fruits size_many fruits good color_good smell_%especially tasty</Title>
            <RowTitlesColumn Width="74">
                <Subcolumn></Subcolumn>
            </RowTitlesColumn>
            <XColumn Width="73" Subcolumns="1" Decimals="0">
                <Title>Times for germination (day)</Title>
            </XColumn>
            <XAdvancedColumn Version="1" Width="73" Decimals="0" Subcolumns="1">
                <Title>Times for germination (day)</Title>
            </XAdvancedColumn>
            <YColumn Width="301" Decimals="1" Subcolumns="5">
                <Title>large_light</Title>
            </YColumn>
            <YColumn Width="301" Decimals="1" Subcolumns="5">
                <Title>large_heavy</Title>
            </YColumn>
            <YColumn Width="301" Decimals="1" Subcolumns="5">
                <Title>small_heavy</Title>
            </YColumn>
            <YColumn Width="350" Decimals="2" Subcolumns="5">
                <Title>small_light</Title>
            </YColumn>
        </Table>
        <Table ID="Table6" XFormat="numbers" YFormat="replicates" Replicates="5" TableType="XY" EVFormat="AsteriskAfterNumber">
            <Title>in the sunny place_fruits size_a few fruits good color_good smell_%especially tasty</Title>
            <RowTitlesColumn Width="74">
                <Subcolumn></Subcolumn>
            </RowTitlesColumn>
            <XColumn Width="73" Subcolumns="1" Decimals="0">
                <Title>Times for germination (day)</Title>
            </XColumn>
            <XAdvancedColumn Version="1" Width="73" Decimals="0" Subcolumns="1">
                <Title>Times for germination (day)</Title>
            </XAdvancedColumn>
            <YColumn Width="301" Decimals="1" Subcolumns="5">
                <Title>large_light</Title>
            </YColumn>
            <YColumn Width="301" Decimals="1" Subcolumns="5">
                <Title>large_heavy</Title>
            </YColumn>
            <YColumn Width="301" Decimals="2" Subcolumns="5">
                <Title>small_heavy</Title>
            </YColumn>
            <YColumn Width="350" Decimals="2" Subcolumns="5">
                <Title>small_light</Title>
            </YColumn>
        </Table>
        <Table ID="Table7" XFormat="numbers" YFormat="replicates" Replicates="5" TableType="XY" EVFormat="AsteriskAfterNumber">
            <Title>in the sunny place_fruits size_many fruits good color_normal or good smell_%especially tasty</Title>
            <RowTitlesColumn Width="74">
                <Subcolumn></Subcolumn>
            </RowTitlesColumn>
            <XColumn Width="73" Subcolumns="1" Decimals="0">
                <Title>Times for germination (day)</Title>
            </XColumn>
            <XAdvancedColumn Version="1" Width="73" Decimals="0" Subcolumns="1">
                <Title>Times for germination (day)</Title>
            </XAdvancedColumn>
            <YColumn Width="301" Decimals="1" Subcolumns="5">
                <Title>large_light(normal smell)</Title>
            </YColumn>
            <YColumn Width="301" Decimals="1" Subcolumns="5">
                <Title>large_heavy(normal smell)</Title>
            </YColumn>
            <YColumn Width="301" Decimals="1" Subcolumns="5">
                <Title>small_heavy(normal smell)</Title>
            </YColumn>
            <YColumn Width="350" Decimals="1" Subcolumns="5">
                <Title>small_light(normal smell)</Title>
            </YColumn>
            <YColumn Width="350" Decimals="1" Subcolumns="5">
                <Title>large_light(good smell)</Title>
            </YColumn>
            <YColumn Width="350" Decimals="1" Subcolumns="5">
                <Title>large_heavy(good smell)</Title>
            </YColumn>
            <YColumn Width="350" Decimals="1" Subcolumns="5">
                <Title>small_heavy(good smell)</Title>
            </YColumn>
            <YColumn Width="350" Decimals="2" Subcolumns="5">
                <Title>small_light(good smell)</Title>
            </YColumn>
        </Table>
        <Table ID="Table9" XFormat="numbers" YFormat="replicates" Replicates="5" TableType="XY" EVFormat="AsteriskAfterNumber">
            <Title>in the sunny place or the shade_fruit size_many fruits good color_good smell_%especially tasty</Title>
            <RowTitlesColumn Width="74">
                <Subcolumn></Subcolumn>
            </RowTitlesColumn>
            <XColumn Width="73" Subcolumns="1" Decimals="0">
                <Title>Times for germination (day)</Title>
            </XColumn>
            <XAdvancedColumn Version="1" Width="73" Decimals="0" Subcolumns="1">
                <Title>Times for germination (day)</Title>
            </XAdvancedColumn>
            <YColumn Width="301" Decimals="1" Subcolumns="5">
                <Title>large_light(in the sunny place)</Title>
            </YColumn>
            <YColumn Width="301" Decimals="1" Subcolumns="5">
                <Title>large_heavy(in the sunny place)</Title>
            </YColumn>
            <YColumn Width="301" Decimals="1" Subcolumns="5">
                <Title>small_heavy(in the sunny place)</Title>
            </YColumn>
            <YColumn Width="350" Decimals="2" Subcolumns="5">
                <Title>small_light(in the sunny place)</Title>
            </YColumn>
            <YColumn Width="350" Decimals="1" Subcolumns="5">
                <Title>large_light(in the shade place)</Title>
            </YColumn>
            <YColumn Width="350" Decimals="1" Subcolumns="5">
                <Title>large_heavy(in the shade place)</Title>
            </YColumn>
            <YColumn Width="350" Decimals="1" Subcolumns="5">
                <Title>small_heavy(in the shade place)</Title>
            </YColumn>
            <YColumn Width="350" Decimals="1" Subcolumns="5">
                <Title>small_light(in the shade place)</Title>
            </YColumn>
        </Table>
        <Table ID="Table10" XFormat="numbers" YFormat="replicates" Replicates="5" TableType="XY" EVFormat="AsteriskAfterNumber">
            <Title>coloq_in the sunny place_fruit size_many fruits good color_good smell_%especially tasty</Title>
            <RowTitlesColumn Width="74">
                <Subcolumn></Subcolumn>
            </RowTitlesColumn>
            <SubColumnTitles OwnSet="0">
                <Subcolumn></Subcolumn>
                <Subcolumn></Subcolumn>
                <Subcolumn></Subcolumn>
                <Subcolumn></Subcolumn>
                <Subcolumn></Subcolumn>
            </SubColumnTitles>
            <XColumn Width="73" Subcolumns="1" Decimals="0">
                <Title>Times for germination (day)</Title>
            </XColumn>
            <XAdvancedColumn Version="1" Width="73" Decimals="0" Subcolumns="1">
                <Title>Times for germination (day)</Title>
            </XAdvancedColumn>
            <YColumn Width="301" Decimals="1" Subcolumns="5">
                <Title>large_light</Title>
            </YColumn>
            <YColumn Width="301" Decimals="1" Subcolumns="5">
                <Title>small_heavy</Title>
            </YColumn>
            <YColumn Width="301" Decimals="2" Subcolumns="5">
                <Title>small_light</Title>
            </YColumn>
        </Table>
        <Table ID="Table11" XFormat="numbers" YFormat="replicates" Replicates="5" TableType="XY" EVFormat="AsteriskAfterNumber">
            <Title>coloq_in the sunny place_fruit size_a few fruits good color_good smell_%especially tasty</Title>
            <RowTitlesColumn Width="74">
                <Subcolumn></Subcolumn>
            </RowTitlesColumn>
            <XColumn Width="73" Subcolumns="1" Decimals="0">
                <Title>Times for germination (day)</Title>
            </XColumn>
            <XAdvancedColumn Version="1" Width="73" Decimals="0" Subcolumns="1">
                <Title>Times for germination (day)</Title>
            </XAdvancedColumn>
            <YColumn Width="301" Decimals="1" Subcolumns="5">
                <Title>large_light</Title>
            </YColumn>
            <YColumn Width="301" Decimals="1" Subcolumns="5">
                <Title>large_heavy</Title>
            </YColumn>
            <YColumn Width="301" Decimals="2" Subcolumns="5">
                <Title>small_heavy</Title>
            </YColumn>
        </Table>
        <Table ID="Table12" XFormat="numbers" YFormat="replicates" Replicates="5" TableType="XY" EVFormat="AsteriskAfterNumber">
            <Title>coloq_in the sunny place_fruit size_many flowers_good smell_%especially tasty</Title>
            <RowTitlesColumn Width="74">
                <Subcolumn></Subcolumn>
            </RowTitlesColumn>
            <SubColumnTitles OwnSet="0">
                <Subcolumn></Subcolumn>
                <Subcolumn></Subcolumn>
                <Subcolumn></Subcolumn>
                <Subcolumn></Subcolumn>
                <Subcolumn></Subcolumn>
            </SubColumnTitles>
            <XColumn Width="40" Subcolumns="1" Decimals="0">
                <Title>Times for germination (day)</Title>
            </XColumn>
            <XAdvancedColumn Version="1" Width="40" Decimals="0" Subcolumns="1">
                <Title>Times for germination (day)</Title>
            </XAdvancedColumn>
            <YColumn Width="301" Decimals="2" Subcolumns="5">
                <Title>many fruits (good smell)</Title>
            </YColumn>
            <YColumn Width="301" Decimals="2" Subcolumns="5">
                <Title>a few fruits (good smell)</Title>
            </YColumn>
        </Table>
        <Table ID="Table13" XFormat="numbers" YFormat="replicates" Replicates="5" TableType="XY" EVFormat="AsteriskAfterNumber">
            <Title>coloq_in the sunny place or the shade_fruit size_many flowers_good smell_%especially tasty</Title>
            <RowTitlesColumn Width="74">
                <Subcolumn></Subcolumn>
            </RowTitlesColumn>
            <XColumn Width="73" Subcolumns="1" Decimals="0">
                <Title>Times for germination (day)</Title>
            </XColumn>
            <XAdvancedColumn Version="1" Width="73" Decimals="0" Subcolumns="1">
                <Title>Times for germination (day)</Title>
            </XAdvancedColumn>
            <YColumn Width="301" Decimals="2" Subcolumns="5">
                <Title>many fruits (sunny)</Title>
            </YColumn>
            <YColumn Width="301" Decimals="2" Subcolumns="5">
                <Title>a few fruits (sunny)</Title>
            </YColumn>
            <YColumn Width="301" Decimals="1" Subcolumns="5">
                <Title>many fruits (shade)</Title>
            </YColumn>
            <YColumn Width="350" Decimals="2" Subcolumns="5">
                <Title>a few fruits (shade)</Title>
            </YColumn>
        </Table>
    </GraphPadPrismFile>
    '''
    root = etree.XML(xml_string.encode('utf-8'), parser=etree.XMLParser(remove_blank_text=True))
    # tree = etree.ElementTree(root)
    # tree.write('D:/1.pzfx', encoding='UTF-8', xml_declaration=True)    
    return root