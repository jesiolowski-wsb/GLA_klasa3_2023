<div data-v-ed1287b8="" data-v-0f3b0a46="" class="question-html-content mb-3 narrow copy-protection d-print-none"><p>A turn-based strategy game has a grid with water and land. The grid contains a <em>True</em> value where it's water and <em>False</em> where it's land.</p>
<p>The player controls a boat unit with a particular movement pattern. It can only move to fixed destinations from its current position as shown in the image below:</p>
<p><img alt="movement pattern" height="330" sizes="(min-width: 590px) 590px, 50vw" src="/resources/media/b2a1f0fa-d196-4892-a89f-690b054f10ab/Empty-Water-PPT-pattern2.jpg" srcset="/resources/media/b2a1f0fa-d196-4892-a89f-690b054f10ab/Empty-Water-PPT-pattern2.jpg 590w, /resources/media/b2a1f0fa-d196-4892-a89f-690b054f10ab/Empty-Water-PPT-pattern2-442.jpg 442w" style="max-height: 330px; max-width: 560px" width="330"></p>
<p>The boat can only move in a direct path through water to the possible destinations, so a destination will become unreachable if there is land in the way.&nbsp;</p>
<p>Implement the <em>can_travel_to</em> function, that checks whether a destination is reachable by the boat. It should return <em>True </em>for destinations that are reachable according to the pattern above, and <em>False </em>for unreachable or out of bounds destinations which are outside the grid.&nbsp;</p>
<p>For example, consider the following code:</p>
<pre><code class="language-python hljs">gameMatrix = [
    [<span class="hljs-literal">False</span>, <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>],
    [<span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>],
    [<span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>],
    [<span class="hljs-literal">False</span>, <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">False</span>, <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>],
    [<span class="hljs-literal">False</span>, <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">True</span>,  <span class="hljs-literal">False</span>, <span class="hljs-literal">True</span>],
    [<span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>, <span class="hljs-literal">False</span>],
]

<span class="hljs-built_in">print</span>(can_travel_to(gameMatrix, <span class="hljs-number">3</span>, <span class="hljs-number">2</span>, <span class="hljs-number">2</span>, <span class="hljs-number">2</span>)) <span class="hljs-comment"># True, Valid move</span>
<span class="hljs-built_in">print</span>(can_travel_to(gameMatrix, <span class="hljs-number">3</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>)) <span class="hljs-comment"># False, Can't travel through land</span>
<span class="hljs-built_in">print</span>(can_travel_to(gameMatrix, <span class="hljs-number">3</span>, <span class="hljs-number">2</span>, <span class="hljs-number">6</span>, <span class="hljs-number">2</span>)) <span class="hljs-comment"># False, Out of bounds</span></code></pre>

<p>The following image shows valid and invalid destinations when the boat is in the position (3, 2):</p>

<p><img alt="terrain movement" height="330" sizes="(min-width: 505px) 505px, 50vw" src="/resources/media/48b1c636-9856-487a-9960-50e592424970/Terrain-PPT-pattern2_small.jpg" srcset="/resources/media/48b1c636-9856-487a-9960-50e592424970/Terrain-PPT-pattern2_small.jpg 505w, /resources/media/48b1c636-9856-487a-9960-50e592424970/Terrain-PPT-pattern2_small-378.jpg 378w" style="max-height: 330px; max-width: 560px" width="329"></p></div>
