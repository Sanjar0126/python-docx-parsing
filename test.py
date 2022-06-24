from lxml import etree
import ziamath as zm


oMathElement = '<m:oMath xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"> <m:rad> <m:radPr> <m:degHide m:val="1"/> <m:ctrlPr> <w:rPr> <w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math" w:cs="Times New Roman"/> <w:i/> <w:sz w:val="24"/> <w:szCs w:val="24"/> <w:lang w:val="en-US"/> </w:rPr> </m:ctrlPr> </m:radPr> <m:deg/> <m:e> <m:sSup> <m:sSupPr> <m:ctrlPr> <w:rPr> <w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math" w:cs="Times New Roman"/> <w:i/> <w:sz w:val="24"/> <w:szCs w:val="24"/> <w:lang w:val="en-US"/> </w:rPr> </m:ctrlPr> </m:sSupPr> <m:e> <m:r> <w:rPr> <w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math" w:cs="Times New Roman"/> <w:sz w:val="24"/> <w:szCs w:val="24"/> <w:lang w:val="en-US"/> </w:rPr> <m:t>t</m:t> </m:r> </m:e> <m:sup> <m:r> <w:rPr> <w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math" w:cs="Times New Roman"/> <w:sz w:val="24"/> <w:szCs w:val="24"/> </w:rPr> <m:t>5</m:t> </m:r> </m:sup> </m:sSup> <m:r> <w:rPr> <w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math" w:cs="Times New Roman"/> <w:sz w:val="24"/> <w:szCs w:val="24"/> </w:rPr> <m:t>+3</m:t> </m:r> </m:e> </m:rad> <m:r> <w:rPr> <w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math" w:cs="Times New Roman"/> <w:sz w:val="24"/> <w:szCs w:val="24"/> </w:rPr> <m:t>-</m:t> </m:r> <m:rad> <m:radPr> <m:degHide m:val="1"/> <m:ctrlPr> <w:rPr> <w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math" w:cs="Times New Roman"/> <w:i/> <w:sz w:val="24"/> <w:szCs w:val="24"/> <w:lang w:val="en-US"/> </w:rPr> </m:ctrlPr> </m:radPr> <m:deg/> <m:e> <m:sSup> <m:sSupPr> <m:ctrlPr> <w:rPr> <w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math" w:cs="Times New Roman"/> <w:i/> <w:sz w:val="24"/> <w:szCs w:val="24"/> <w:lang w:val="en-US"/> </w:rPr> </m:ctrlPr> </m:sSupPr> <m:e> <m:r> <w:rPr> <w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math" w:cs="Times New Roman"/> <w:sz w:val="24"/> <w:szCs w:val="24"/> <w:lang w:val="en-US"/> </w:rPr> <m:t>t</m:t> </m:r> </m:e> <m:sup> <m:r> <w:rPr> <w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math" w:cs="Times New Roman"/> <w:sz w:val="24"/> <w:szCs w:val="24"/> </w:rPr> <m:t>5</m:t> </m:r> </m:sup> </m:sSup> <m:r> <w:rPr> <w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math" w:cs="Times New Roman"/> <w:sz w:val="24"/> <w:szCs w:val="24"/> </w:rPr> <m:t>-2</m:t> </m:r> </m:e> </m:rad> <m:r> <w:rPr> <w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math" w:cs="Times New Roman"/> <w:sz w:val="24"/> <w:szCs w:val="24"/> </w:rPr> <m:t>=1</m:t> </m:r> </m:oMath>'
# oMathElement = '<m:oMath xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"> <m:r> <w:rPr> <w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math" w:cs="Times New Roman"/> <w:sz w:val="24"/> <w:szCs w:val="24"/> </w:rPr> <m:t>=1</m:t> </m:r> </m:oMath>'
math2 = '<m:oMath xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math" w:cs="Times New Roman"/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr><m:t>2</m:t></m:r><m:sSup><m:sSupPr><m:ctrlPr><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math" w:cs="Times New Roman"/><w:i/><w:sz w:val="24"/><w:szCs w:val="24"/><w:lang w:val="en-US"/></w:rPr></m:ctrlPr></m:sSupPr><m:e><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math" w:cs="Times New Roman"/><w:sz w:val="24"/><w:szCs w:val="24"/><w:lang w:val="en-US"/></w:rPr><m:t>x</m:t></m:r></m:e><m:sup><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math" w:cs="Times New Roman"/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr><m:t>2</m:t></m:r></m:sup></m:sSup><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math" w:cs="Times New Roman"/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr><m:t>-26</m:t></m:r><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math" w:cs="Times New Roman"/><w:sz w:val="24"/><w:szCs w:val="24"/><w:lang w:val="en-US"/></w:rPr><m:t>x</m:t></m:r><m:r><w:rPr><w:rFonts w:ascii="Cambria Math" w:hAnsi="Cambria Math" w:cs="Times New Roman"/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr><m:t>+72=0</m:t></m:r></m:oMath>'

namespaces = {
            'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
            'wp':'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
            'a':'http://schemas.openxmlformats.org/drawingml/2006/main',
            'pic':'http://schemas.openxmlformats.org/drawingml/2006/picture',
            'r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
            'm':"http://schemas.openxmlformats.org/officeDocument/2006/math",
        }

tree = etree.fromstring(oMathElement)

xslt_root = etree.parse("./OMML2MML.XSL")
mml_transform = etree.XSLT(xslt_root)
mml = mml_transform(tree)

xml_string = etree.tostring(mml).decode("utf-8")

svg_math = zm.Math(xml_string)

svg_math.save("images/svg.svg")