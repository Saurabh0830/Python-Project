#############################################################################
# Generated by PAGE version 4.13
# in conjunction with Tcl version 8.6
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #d8d8d8
set vTcl(active_menu_fg) #000000
}

#############################################################################
# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family {Segoe UI Black} -size 12 -weight bold -slant italic -underline 0 -overstrike 0" \
    user \
    vTcl:font10
vTcl:font:add_font \
    "-family {Segoe UI Black} -size 11 -weight bold -slant italic -underline 0 -overstrike 0" \
    user \
    vTcl:font9
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top37
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top37
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    set site_3_0 $base.fra39
    set site_3_0 $base.fra46
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top37 {base} {
    if {$base == ""} {
        set base .top37
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background {#d9d9d9} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 923x599+592+140
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1055
    wm minsize $top 148 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "View_Ordered"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    frame $top.fra38 \
        -borderwidth 10 -relief groove -background {#c4632b} -height 435 \
        -highlightbackground {#d9d9d9} -highlightcolor black -width 905 
    vTcl:DefineAlias "$top.fra38" "ViewOrder" vTcl:WidgetProc "Toplevel1" 1
    frame $top.fra39 \
        -borderwidth 10 -relief groove -background {#c4632b} -height 65 \
        -highlightbackground {#d9d9d9} -highlightcolor black -width 905 
    vTcl:DefineAlias "$top.fra39" "Frame2" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra39
    label $site_3_0.lab40 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#c4632b} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Name 
    vTcl:DefineAlias "$site_3_0.lab40" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab41 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#c4632b} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text PNO 
    vTcl:DefineAlias "$site_3_0.lab41" "Label1_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab42 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#c4632b} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Price 
    vTcl:DefineAlias "$site_3_0.lab42" "Label1_2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab43 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#c4632b} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Quantity 
    vTcl:DefineAlias "$site_3_0.lab43" "Label1_3" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab44 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#c4632b} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -text Total 
    vTcl:DefineAlias "$site_3_0.lab44" "Label1_4" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab40 \
        -in $site_3_0 -x 30 -y 20 -width 102 -relwidth 0 -height 26 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab41 \
        -in $site_3_0 -x 210 -y 10 -width 102 -height 26 -anchor nw \
        -bordermode inside 
    place $site_3_0.lab42 \
        -in $site_3_0 -x 380 -y 10 -width 102 -height 26 -anchor nw \
        -bordermode inside 
    place $site_3_0.lab43 \
        -in $site_3_0 -x 560 -y 10 -width 102 -height 26 -anchor nw \
        -bordermode inside 
    place $site_3_0.lab44 \
        -in $site_3_0 -x 740 -y 10 -width 102 -height 26 -anchor nw \
        -bordermode inside 
    frame $top.fra46 \
        -borderwidth 10 -relief groove -background {#c4632b} -height 75 \
        -highlightbackground {#d9d9d9} -highlightcolor black -width 905 
    vTcl:DefineAlias "$top.fra46" "Frame3" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra46
    button $site_3_0.but47 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command Total_Q -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {Total Quantity :} 
    vTcl:DefineAlias "$site_3_0.but47" "Button1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab48 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#c4632b} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black 
    vTcl:DefineAlias "$site_3_0.lab48" "TotalQuantity" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but49 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command Total_T -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font9,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black -pady 0 \
        -text {Total Cost :} 
    vTcl:DefineAlias "$site_3_0.but49" "Button1_7" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab50 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#c4632b} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black 
    vTcl:DefineAlias "$site_3_0.lab50" "TotalCost" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.but47 \
        -in $site_3_0 -x 30 -y 20 -width 156 -relwidth 0 -height 33 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab48 \
        -in $site_3_0 -x 180 -y 10 -width 102 -height 26 -anchor nw \
        -bordermode inside 
    place $site_3_0.but49 \
        -in $site_3_0 -x 570 -y 10 -width 156 -height 33 -anchor nw \
        -bordermode inside 
    place $site_3_0.lab50 \
        -in $site_3_0 -x 730 -y 10 -width 102 -height 26 -anchor nw \
        -bordermode inside 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra38 \
        -in $top -x 10 -y 70 -width 905 -relwidth 0 -height 435 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.fra39 \
        -in $top -x 10 -y 10 -width 905 -relwidth 0 -height 65 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.fra46 \
        -in $top -x 10 -y 490 -width 905 -relwidth 0 -height 75 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top37 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

