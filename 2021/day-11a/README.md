# --- Day 11: Dumbo Octopus ---

You enter a large cavern full of rare bioluminescent [dumbo octopuses](https://www.youtube.com/watch?v=eih-VSaS2g0)! They seem to not like the Christmas lights on your submarine, so you turn them off for now.

There are 100 octopuses arranged neatly in a 10 by 10 grid. Each octopus slowly gains **energy** over time and **flashes** brightly for a moment when its energy is full. Although your lights are off, maybe you could navigate through the cave without disturbing the octopuses if you could predict when the flashes of light will happen.

Each octopus has an **energy level** - your submarine can remotely measure the energy level of each octopus (your puzzle input). For example:

```text
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
```

The energy level of each octopus is a value between `0` and `9`. Here, the top-left octopus has an energy level of `5`, the bottom-right one has an energy level of `6`, and so on.

You can model the energy levels and flashes of light in **steps**. During a single step, the following occurs:

- First, the energy level of each octopus increases by `1`.
- Then, any octopus with an energy level greater than `9` **flashes**. This increases the energy level of all adjacent octopuses by `1`, including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than `9`, it **also flashes**. This process continues as long as new octopuses keep having their energy level increased beyond `9`. (An octopus can only flash **at most once per step**.)
- Finally, any octopus that flashed during this step has its energy level set to `0`, as it used all of its energy to flash.

Adjacent flashes can cause an octopus to flash on a step even if it begins that step with very little energy. Consider the middle octopus with `1` energy in this situation:

```text
Before any steps:
11111

19991

19191

19991

11111


After step 1:

34543
 vvv
40004
 vvv
50005
 vvv
40004

34543


After step 2:

45654

51115

61116

51115

45654
```

An octopus is **highlighted** when it flashed during the given step.

Here is how the larger example above progresses:

```text
Before any steps:

5483143223

2745854711

5264556173

6141336146

6357385478

4167524645

2176841721

6882881134

4846848554

5283751526


After step 1:

6594254334

3856965822

6375667284

7252447257

7468496589

5278635756

3287952832

7993992245

5957959665

6394862637


After step 2:
  v
8807476555
 v  v  v
5089087054
        v
8597889608
        vv
8485769600
  vv v  vv
8700908800
  vvv
6600088989
  vvvv
6800005943
vvvvvv
0000007456
 vvvvvv
9000000876
  vvvv
8700006848


After step 3:
vv v vv
0050900866
  vv vv
8500800575
  vvvvvv
9900000039
  vvvvvv
9700000041
    v vv
9935080063
     vvvvv
7712300000
      vvv
7911250009
      vvvv
2211130000
v      vvv
0421125000
vv     vvv
0021119000


After step 4:
    v
2263031977
v   v
0923031697
vv       v
0032221150
vv
0041111163
vv
0076191174
vv
0053411122
vv       v
0042361120

5532241122

1532247211
      v
1132230211


After step 5:
       vvv
4484144000
 v     vvv
2044144000

2253333493

1152333274
     v
1187303285

1164633233

1153472231

6643352233

2643358322

2243341322


After step 6:

5595255111

3155255222
        v
3364444605

2263444496

2298414396

2275744344

2264583342

7754463344

3754469433

3354452433


After step 7:
  v
6707366222

4377366333

4475555827
        v
3496655709
  vv    v
3500625609
  v
3509955566

3486694453

8865585555
      v
4865580644

4465574644


After step 8:

7818477333

5488477444

5697666949
  v      v
4608766830
         v
4734946730
   vv
4740097688
  vvvv
6900007564
vvvvvv
0000009666
 vvvvv
8000004755
  vvvv
6800007755


After step 9:
 v vvvv
9060000644
  vvvvv
7800000976
  vvvvvv v
6900000080
   vvvvv
5840000082
    vvvv
5858000093
     vvvvv
6962400000
 v    vvv
8021250009
      vvv
2221130009
       v
9111128097

7911119976


After step 10:
v
0481112976
vv     vv
0031112009
vv      v
0041112504
vv      v
0081111406
vv      v
0099111306
vv
0093511233
v        v
0442361130
         v
5532252350
v     v vv
0532250600
vv    vvvv
0032240000
```

After step 10, there have been a total of `204` flashes. Fast forwarding, here is the same configuration every 10 steps:

```text
After step 20:

3936556452
        v
5686556806
         v
4496555690
         v
4448655580
         v
4456865570
   vv
5680086577
 vvvvv
7000009896
vvvvvvv
0000000344
 vvvvvv
6000000364
  vvvv
4600009543


After step 30:
v
0643334118

4253334611

3374333458

2225333337

2229333338

2276733333

2754574565

5544458511

9444447111

7944446119


After step 40:

6211111981
v
0421111119
vv
0042111115
vvv
0003111115
vvv
0003111116
vv
0065611111
v
0532351111

3322234597

2222222976

2222222762


After step 50:

9655556447
        v
4865556805
         v
4486555690
         v
4458655580
         v
4574865570
  vvv
5700086566
 vvvvv
6000009887
 vvvvvv
8000000533
  vvvvv
6800000633
   vvvv
5680000538


After step 60:
        vv
2533334200
         v
2743334640

2264333458

2225333337

2225333338

2287833333

3854573455

1854458611

1175447111

1115446111


After step 70:

8211111164
v
0421111166
vv
0042111114
vvv
0004211115
vvvv
0000211116
vv
0065611111
v
0532351111

7322235117

5722223475

4572222754


After step 80:

1755555697
        v
5965555609
         v
4486555680
         v
4458655580
   v     v
4570865570
  vvv
5700086566
 vvvvv
7000008666
vvvvvvv  v
0000000990
vvvvvvv vv
0000000800
vvvvvvvvvv
0000000000


After step 90:

7433333522

2643333522

2264333458

2226433337

2222433338

2287833333

2854573333

4854458333

3387779333

3333333333


After step 100:
v
0397666866
v
0749766918
vv
0053976933
vvv
0004297822
vvv
0004229892
vv
0053222877
v
0532222966

9322228966

7922286866

6789998766
```

After 100 steps, there have been a total of **`1656`** flashes.

Given the starting energy levels of the dumbo octopuses in your cavern, simulate 100 steps. **How many total flashes are there after 100 steps?**
