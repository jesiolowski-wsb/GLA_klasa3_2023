<div><p>Hipotetyczna gra turowa ze statkiem poruszającym się w określony sposób. Siatka / plansza zawiera wartości <em>True</em> jeśli na pozycji znajduje się woda oraz <em>False</em> jeśli na pozycji znajduje się suchy ląd.</p>
<p>Gracz kontroluje łódź w ściśle określonny sposób. Jednostka może poruszać się po planszy jedynie po linii prostej i o określoną ilość pól (w zależności od kierunku)</p>
<p>
<img width="297" alt="image" src="https://github.com/jesiolowski-wsb/GLA_klasa3_2023/assets/67168776/7968d6d7-650f-4148-9157-04ace31a433b">

</p>
<p>The boat can only move in a direct path through water to the possible destinations, so a destination will become unreachable if there is land in the way.&nbsp;</p>
<p>Implement the <em>can_travel_to</em> function, that checks whether a destination is reachable by the boat. It should return <em>True </em>for destinations that are reachable according to the pattern above, and <em>False </em>for unreachable or out of bounds destinations which are outside the grid.&nbsp;</p>
<p>Jako przykład, kod poniżej:</p>
<pre><code class="language-python hljs">gameMatrix = [
    [<span class="hljs-literal">False</span>, <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>],
    [<span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>],
    [<span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>],
    [<span class="hljs-literal">False</span>, <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">False</span>, <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>],
    [<span class="hljs-literal">False</span>, <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">False</span>, <span class="hljs-literal">True</span>],
    [<span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>],
]

<span class="hljs-built_in">print</span>(can_travel_to(gameMatrix, <span class="hljs-number">3</span>, <span class="hljs-number">2</span>, <span class="hljs-number">2</span>, <span class="hljs-number">2</span>)) <span class="hljs-comment"># True, ruch jest dopuszczalny</span>
<span class="hljs-built_in">print</span>(can_travel_to(gameMatrix, <span class="hljs-number">3</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>)) <span class="hljs-comment"># False, nie można przepłynąć przez ląd</span>
<span class="hljs-built_in">print</span>(can_travel_to(gameMatrix, <span class="hljs-number">3</span>, <span class="hljs-number">2</span>, <span class="hljs-number">6</span>, <span class="hljs-number">2</span>)) <span class="hljs-comment"># False, poza dopuszczalnym zakresem</span></code></pre>

<p>Obrazek poniżej ilustruje wszystkie dopuszczalne ruchy wynikające ze statku na pozycji (3, 2):</p>

<p><img width="297" alt="image" src="https://github.com/jesiolowski-wsb/GLA_klasa3_2023/assets/67168776/e408e14c-7198-4f28-a5b5-90e02b4cd48f">
</p></div>
