---
layout: page
title: Tutoring
---

# Math Tutoring by Abhay

Math doesn't need to be difficult; it's just a muscle that we need to work out like any other. If you're ready to improve your math skills, build confidence, and ace any upcoming tests, you're in the right place! For quick answers to common questions, skip to any of the following sections:

* [Classes](#classes)
* [Pricing](#pricing)
* [Evidence](#evidence)
* [Register](#register)

## Classes

I offer math tutoring in any math class from pre-algebra onwards. Here are classes that I've *taught* (at a school or university):

* Calculus I
* Calculus II
* Calculus III
* Real Analysis I

and classes that I've only *tutored*:

* Algebra I
* Algebra II
* Geometry
* Precalculus

But these lists are not exhaustive. If you're unsure if I'm willing and able to tutor for your class, feel free to [reach out](#register) anyway.

## Pricing

The pricing model depends on your goals. I have different pricing for short-term test prep, long-term skill building, and extra advancement. All three models have a base price for 1-1 tutoring, along with a smaller fee for additional students. If you need the direct attention, schedule individual sessions with me; but if you're more interested in splitting the cost with a group of friends, choose one of the small-group options.

Finding a tutor that fits your needs is difficult but important, so I will do a single 1-hour session free of charge for anyone unsure if I'm the right person for you.

#### Test prep

If you're preparing for a test, we will plan our sessions as frequently as you need at a cost of $75/hr for 1-1 lessons. This allows for extra flexibility for you so we can cram if needed with multiple sessions in the same week for as long as needed.

I will also allow for additional students up to a maximum group size of 8 people at a charge of an extra $15/hr per added student. So if you and your two friends are all prepping for the same test, I can tutor you all together for $105/hr, which works out to just $35/hr for each of you.

#### Skill-building

If you're more interested in longterm skill-building, this is the option for you! For this option, we plan 1-2 weekly sessions based on your availability and you prepay for the full set of 4-32 sessions at a rate of $50/hr. *Note:* I do not accept fewer than 4 sessions at this rate because the intention is to build your skills over the long term, and I take more detailed notes on your progress, strengths, and weaknesses.

I will also allow for additional students up to a maximum group size of 14 people at a charge of an extra $8/hr per added student. So if you and your five friends are all in the same class, I can tutor you all together for $90/hr, which works out to just $15/hr for each of you.

#### Advancement

Finally, if you're interested in learning something entirely new, I also accept students by interview. These are highly specific and depend on your specific case, but pricing ranges from $10/hr to $50/hr depending on your interest, my availability, and my prior understanding (as this influences the work I do outside of our meetings).

#### Summary

That was a lot of info, so use the tool below to see pricing based on your specific case.

<div>
<script type="text/javascript">
function setup() {
	var a = document.getElementById('studin');
    var b = document.getElementById('sessin');
    if (document.getElementById('test').checked) {
    	a.min = 1; a.max = 8;
        b.min = 1; b.max = 40;
    } else if (document.getElementById('long').checked) {
    	a.min = 1; a.max = 14;
        b.min = 4; b.max = 32;
    } else if (document.getElementById('adv').checked) {
    }
    update();
}

function update() {
	var n = document.getElementById('studin').value;
    var m = document.getElementById('sessin').value;
	document.getElementById('stud').value = n;
	document.getElementById('sess').value = m;
    var a = document.getElementById('tot');
    var b = document.getElementById('price');
    var c = document.getElementById('perstud');
    var d = document.getElementById('totps');
    if (document.getElementById('test').checked) {
    	a.value = '$'+((60+15*n)*m);
        b.value = '$'+(60+15*n);
        c.value = '$'+(15+60.0/n).toFixed(2);
        d.value = '$'+(15*m+60.0*m/n).toFixed(2)
    } else if (document.getElementById('long').checked) {
    	a.value = '$'+((42+8*n)*m);
        b.value = '$'+(42+8*n);
        c.value = '$'+(8+42.0/n).toFixed(2);
        d.value = '$'+(8*m+42.0*m/n).toFixed(2);
    } else if (document.getElementById('adv').checked) {
    	a.value = "Let's talk!";
        b.value = "Let's talk!";
        c.value = "Let's talk!";
        d.value = "Let's talk!";
    }
}
</script>

  Class type:
  <input type="radio" name="cls" id="test" onclick="setup()">
  <label for="test">Test Prep</label>
  <input type="radio" name="cls" id="long" onclick="setup()">
  <label for="long">Longterm skill-building</label>
  <input type="radio" name="cls" id="adv" onclick="setup()">
  <label for="adv">Advancement</label>

  <br>
  Number of students: <input type="range" id="studin" min="1" max="8" value="1" step="1" oninput="update()"><output id="stud">1</output><br>
  Number of (hour-long) sessions: <input type="range" id="sessin" min="1" max="32" value="1" step="1" oninput="update()"><output id="sess">1</output><br>
  Total price: <output id="tot"></output><br>
  Total price per student: <output id="totps"></output><br>
  Hourly price: <output id="price"></output><br>
  Hourly price per student: <output id="perstud"></output><br>
 </div>


## Evidence

You're spending a lot of time and money by choosing to work with me, so you deserve to know why you should expect that it works! First: my credentials. I am currently in my 4th year in the Ph.D. program at the Math Department of the University of Utah. But this is evidence that I can *do* math, not that I can *teach* math. Here are some quotes from students in classes I've taught in the past:

* "Absolutely phenomenal person. They are extremely supportive and will break down problems meeting you on your level. They're extremely smart but never abuse it or make you feel stupid if you are struggling with a certain topic."
* "Abhay is a really good teacher and clearly knows what he's doing in terms of content mastery. However, Abhay is also able to translate that complete understanding into something digestible for students, which is a strength that not all teachers have."
* "Honestly the most understanding, compassionate, and fair math professors I’ve had at the U. Teaches content thoroughly and always come so prepared!"

Finally, if it's useful, here's my latest [RateMyProfessor page](https://www.ratemyprofessors.com/professor/2989927): 

## Register

Learned enough and ready to get scheduling? Didn't find the answer to your question here but have one you want to ask me? Either way, [send me a message](https://docs.google.com/forms/d/e/1FAIpQLSdznyrAxqXktGBCVxg8MeRnSEeeTYaq_yFhyZgpnamxpXye5g/viewform?usp=sharing&ouid=109740590401628767205)! 
