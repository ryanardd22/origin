# Independent QA — final artifact review

Reviewed 2026-11-04. Verdict: **PASS for sampled visual review and technical format of this animated storyboard. Audio listening review remains NOT PERFORMED.** No blocking visual or story issue was found in the inspected final-file samples. This is not an unqualified full audiovisual PASS.

Artifact: `out/tombol-save-preview.mp4`, 14,783,459 bytes.
SHA-256: `35d15d29610600378c42ac1e3674661050c560534893aa01793a8d8b02e18f75`.

## Evidence actually inspected

- Source: `src/Video.tsx`, `public/edit-data.json`, `storyboard/voiceover.txt`, relevant board sheets, production README/state, failed transcription-check result.
- Actual final MP4: independently ran ffprobe and extracted additional frames directly from this file. Independently confirmed H.264, yuv420p, 720×1280, 30/1fps, 1500 frames, 50.000000s; AAC stereo audio at 48000Hz.
- Main editor's `out/qa/technical-report.json` reports full decode passed. Reviewer did not independently repeat the complete decode or watch continuous playback.
- Viewed fresh `contact-01.jpg` through `contact-03.jpg`, covering all 24 shot midpoints; opened individual shot images 01, 07, 13, 20, 21, 23 and 24 for close inspection. Viewed all 16 supplied transition-boundary frames in a reviewer-assembled contact sheet.
- Independently extracted and viewed final-MP4 frames 315, 570, 1450 and 1499, checking long captions and the last-frame hold. Temporary review images are `/tmp/tombol-save-review-01.jpg` through `04.jpg`; the boundary overview is `/tmp/tombol-save-boundaries.jpg`.
- Earlier `out/check-opening.png` was stale and was excluded as final evidence. Its former four-word opening caption was replaced successfully in the actual final MP4. Missing sheet 6 was resolved: actual final shots 21–24 are present and visible.

## Visual and story result

- All 24 midpoint scenes are present. No unintended blank frame, storyboard grid, neighboring-panel bleed or severe crop was found in the inspected samples/boundaries.
- Opening title and regrouped opening caption fit the frame. Long caption examples “Lalu manusia mengembangkan”, “Percetakan membantu memperbanyak”, “meninggalkan petunjuk untuk”, and “memeriksa jawabannya.” remain readable with adequate contrast and visible margins. No caption truncation was observed in inspected final frames.
- Shot 13 framing preserves the pencil/diagram action and a readable caption. Shot 20's ellipse marks the missing center of the bridge rather than the narrator or an unrelated region. Shot 21 has no inherited error ellipse. The subsequent book and corrected-diagram images communicate checking and correction.
- Final shot 24 and frame 1499 retain the legible question “Pengetahuan apa yang kamu wariskan?”; no blank end frame was observed. Spoken-caption text has ended by then, leaving the question to hold visually.
- Source has 24 contiguous shots from frame 0 through 1499 and no overlapping caption intervals. Last aligned word ends at 48.011s, last caption at 48.100s. Source narration WAV is 48.160188s and source music WAV is 50.000000s, leaving roughly 1.84s of visual/music hold after narration; there is no duration-based indication of speech truncation.
- Oral knowledge → writing → copying/printing → shared testing → computers/internet → AI → checking answers is coherent. “Semacam tombol save” is a clear metaphor. The hypothetical opening is qualified by later language that oral knowledge *can* disappear when not transmitted. The script makes no fabricated date, named-inventor claim, AI accuracy guarantee or commercial promise.
- Historical scenes are stylized allegory with recurring characters, not precise historical reconstruction. This does not block the approved broad educational metaphor.

## Limits that must remain explicit in delivery

1. **Animated storyboard:** generated still panels receive pan/zoom camera motion and graphical overlays. There is no generated natural body/character motion. Do not present it as full character animation or successful generative-video output. README, state and `media_scope` correctly disclose this distinction.
2. **Audio measured, not listened to:** this reviewer did not hear the narration or music. Main editor reports loudness/peak measurements; these do not establish pronunciation, intelligibility, emotional delivery or subjective music balance. `audio-transcription-check.json` records HTTP 503, not successful transcription validation. No human listening is established by this review.
3. **Sampling, not full playback:** actual final-file metadata and specified frame samples were inspected. Continuous motion smoothness and precise audible word sync were not assessed by playback. Full decode success is recorded by the main editor's technical report.
4. **No social publication:** project records say it has not been uploaded/published to social platforms. This review performs no upload and establishes no publication or user approval of the fallback format.

Review changed only this report and temporary QA images; no source or media changes were made by the reviewer.
