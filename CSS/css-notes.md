
![alt text](https://github.com/deadzg/knowledge-share/blob/master/CSS/css-decision-flow.png)

The styles provided by browser are called user-agent styles (Default behaviour which browser provides to h1, h2, p, li, ul etc)
What we add are author styles (author origin)

Check CSS feature based on browser
https://caniuse.com/

Generate code for centring elements in CSS
http://howtocenterincss.com/

Origin
Priority based on origin: Author Important > Author > User-agent

Specificity
* Styles applied inline
    * Inine style override stylesheet css
    * In order to override inline style add !important to stylesheet css
    * If !important is added to inline style, nothing can be overrriden
* Styles applied using a selector
* Specificity: ID Selector > Class Selector  > Tag/Type selector
* If a selector has more IDs, it wins
* If that results in a tie, the selector with more classes wins
* If that results in a tie, the selector with more tag names wins
* Psuedo class selectors (eg: :hover) and attribute selectors (eg: [type=“input”]) each have the same specificity as a class selector
* The universal selector (*) and combinators (>, +, ~) have no effect on specificity
* If you need to override a style applied using an ID, use another ID
* Specificity Notation: inline, id, classes, tags eg: 1, 2,0,0 (inline, 2 IDs, 0 classes, 0 tags)
* Best Practice: It’s good to keep the specifictiy low, so that if someone wants to override later, it becomes easy to do so
* Best Practice: Don’t use IDs as it increases the specifictiy and it’s diffcult to override it and we may need to add one more class to override it
* Best Practice: Don’t use !important. It’s even more difficult to override than ID and once you use it everytime you need to add if you want to override the original declaration

Source Order
* If origin and specificity are same, then declaration that appears later in the stylesheet or appears in a stylesheet included later on the page takes precendence
* Link styles: LoVe/HAte : L-> a:link , V -> a:visited, H-> a:hover , A -> a:active

Cascaded Value
* The browser follows three steps: origin, specificity, source order to resolve every property for every element on the page. The obtained value is called cascaded value.

Inheritance
* If an element has no cascasded property it may inherit one from the ancestor
* Not all the properties are inherited
* The inheritance will pass from element to element until it’s overriden by a cascade value

Special Values
* You can use inherit and initial to manipulate the cascade
* When a cascaded value is preventing to inherit the property value from parent, inherit can be used
* Every property has an intial or default value. If you assign value initial to the property, then it effectively sets it to default value

Shorthand Properties
* It let’s us set the values of several other properties at one time
    * Eg: font is a shorthand property for: font-style, font-weight, font-size, line-height, font-family
    * Eg: background
    * Eg: border
    * Eg: border-width
* Though shorthand properties let you omit certain values, it implcitly sets the ommitted values to initial values. Thus it may silently override styles you specify elsewhere
* For eg: padding: 12px, 5px, 6px: If the declaration ends before one of the four sides is given value, that side takes its value from the opposite side. So value of left would be 5px
* Properties which only supports two values goes with catesian ie. x and y : Eg: box-shadow, background-position, text-shadow
* Properties with four values go clockwise from top

Relative Units
* One of the most familiar and probably easiest to work with, is pixels. These are known as absolute units i.e. 5px always means the same thing. Other units such as em and rem are not absolute, but relative. The value of relative units changes based on external factors.
* As the user resizes the browser window, your css needs to adjust. This means that the styles can't be applied when you create the page; the browser must calculate them. We need to begin thinking about responsive design.
* Values declared using relative units are evaluated by the browser to an absolute value, called the "computed value".
* Ems
    * 1 em means the font-size of the current element.
    * It exact value varies depending on the element you are applying it to.
    * Convenient for: padding, height, width, border-radius.
    * Default font-size for most browsers is 16px.
```
box {
  padding: 1em;
  border-radius: 1em;
  background-color: lightgray;
}
.box-small {
  font-size: 12px;
}
.box-large {
  font-size: 18px;
}    
```
* Using ems to define font-size
    * font-size ems are derived from the inherited font-size.
* Rems
    * When the browser parses an HTML document, it creates the representation in memory called DOM(tree structure).
    * Root node is the ancestor of all the elements in the document. It has a special pseudo-class selector ":root".
    * ":root" is equivalent to the type selector "html".
    * Rem is short for root em.
    * Instead of being relative to current element, rems are relative to the root element
    * It can be specified using psuedo class eg.     :root {font-size:1em} It wil take browser default ie. 16px.      ul {font-size: .8 rem}
* Best Practice: Use rems for font-sizes, pixels for borders; Use ems paddings, margins and border-radius
* Anti-pattern: Reset font size at page’s root eg: html {font-size: .625em}. It sets the default font-size from 16 * 0.625 px  = 10 px. People do it for easier calculation. Two drawbacks: 1) 10px is too small and we may end up writing more font-size for different tags . 2) You are still thinking in terms of pixels

Viewport-relative units
* Viewport: The framed area in the browser window where the web page is visible
    * vh : 1/100th of the viewport height
    * vw: 1/100th of viewport width
    * vmin : 1/100th of the smaller dimension, height or width
    * vmax: 1/100th of the larger dimension height or width
* Calc
    * The calc() function lets you do basic arithmetic with two or more values.
    * This is par- ticularly useful for combining values that are measured in different units.
    * This function supports addition (+), subtraction (-), multiplication (*) and division (/).
    * The operators must be surrounded by whitespace.
    * Eg.  :root {font-size: calc(0.5em + 1vw)}

Unitless numbers and line-height
* Some properties allow for unitless values. Eg: line-height, z-index, font-weight
* line-height property uses unit as well as unitless values
* Best Practice: Use unitless numbers because they are inherited differently

Custom Properties (CSS Variables)
* You can declare a variable and assign it a value. Then you can use this value throughout the stylesheet
* Eg.   :root {- -main-font: Helvetica, Arial, sans-serif; - - brand-color:#369}
* The name must begin with two hyphens followed by variable name
* To use it.  p {font-family: var(- -main-font); color: var(- -brand-color )}
* var() function accepts a second param, which specifies a fallback value. If the variable specified in the first param is not defined, then the second value is used instead
* p {font-family: var(- -main-font);color: var ( - - brand-color, blue);}
* It helps us define a value in one place, “single source of truth” and reuse the variable throughout the sheet
* If var() function evaluates to an invalid value, the property will be set to its initial value
* You can define the same variable inside multiple selectors and the variable will have a different value for various parts of the page
* Custom properties can be changed using javascript as well

Mastering the Box Model
* Best Practice: For some site designs, the background color of several containers might be transparent. When this is the case, it might be helpful to temporarily apply a background color to the container until you get it sized and positioned accordingly
* Default behaviour of box-model: When you are setting width/height of its content; any padding, border and margins are then added to that width
*
* In order to override the above behaviour:  box-sizing: border-box instead of content-box. With this model, padding doesn’t make an element wider; it makes the innter content narrower. content + padding + border
* * => universal selector  eg. * {box-sizing: border-box}
* In order to apply any style to all elements + psuedo elements of all types eg: *, ::before, :: after {box-sizing: border-box} . With this css, if you are using third party components with their own css, you may see some broken layout if the CSS wasn’t writted with this fix in mind. To fix this. :root {box-sizing: border-box} *,::before, ::after {box-sizing: inherit} .third-party-component {box-sizing: content-box}
* Normal document flow refers to the default layout behaviour of elements on the page. Inline elements flow along with the text of the page, from left to right, line wrapping when they reach the edge of their container. Block-level elements fall on individual lines, with a line break above and below
* When the height of an element is explicitly set, you run the risk of it's content overflowing the container
* Overflow behaviour:
    * visible (default value) : All content visible, even when it overflows container's edge
    * hidden : Content that overflows the container's padding edge is clipped and won't be visible
    * scroll : Scrollbars are added to the containers so the user can scroll to see the remaining content
    * auto : Scrollbars are added to the container only if the contents overflow
* Best Practice: Prefer auto over scroll,as we don't want to show scrollbars unnecessarily
* Control horizontal overflow using overflow-x . Use case: long URL   
* Control verticle overflow using overflow-y
* Bad Practice : Explicitly setting both x and y to different values tends to have unpredictable results
* Bad Practice: Never specify height in percentage. Reason: Percentage refers to the size of element's containing block; the height of that container is determined by the height of its children. This produces a circular definition that the browser cannot resolve, so it will ignore the declaration. For this to work, the parent must have an explicit height.
* Use cases: Container to fill the screen. Use vh units ie. 100vh  =>height of the viewport
* Use case: Create columns of equal height
    * Method 1: Parent of column display:table . By default the table won't expand to 100% width like a block element, so we need to declare width explictly to 100%.  Each column display:table-cell with the required width percentage. Use border-spacing to give margin as the table-cell doesnot respect margin
    * Method 2: **Using Flexbox** ->
        * Using flexbox produces elements of equal height
        * Best Practice: Favor the use of flexbox instead of table layout if you aren't actively supporting IE9 or older
        * Give parent container display: flex
* Bad Practice: Never explicitly set the height of the element unless no other choice is left
* min-height : The element will be atleast as high as you specify and if it doesnot fit, the browser will allow the element to grow naturally to prevent overflow
* max-height: Allows an element to size naturally up to a point, post that the content will overflow.
* Similar is the behaviour for **min-width** and **max-width**
* Vertical Centering
    * vertical-align declaration only affects inline and table-cell elements
    * For block elements give equal amount of padding at top and bottom to center the content
