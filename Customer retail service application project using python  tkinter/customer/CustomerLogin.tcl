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
    "-family {Segoe UI Black} -size 15 -weight bold -slant italic -underline 0 -overstrike 0" \
    user \
    vTcl:font10
vTcl:font:add_font \
    "-family {Segoe UI Black} -size 12 -weight bold -slant italic -underline 0 -overstrike 0" \
    user \
    vTcl:font11
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
    set site_3_0 $base.fra38
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
        -background {#d9d9d9} 
    wm focusmodel $top passive
    wm geometry $top 462x381+788+150
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
    wm title $top "Customer_Login"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    frame $top.fra38 \
        -borderwidth 10 -relief groove -background {#c4632b} -height 365 \
        -width 445 
    vTcl:DefineAlias "$top.fra38" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra38
    label $site_3_0.lab39 \
        -background {#c4632b} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font10,object) -foreground {#000000} \
        -text Login/Registration 
    vTcl:DefineAlias "$site_3_0.lab39" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab40 \
        -background {#c4632b} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font11,object) -foreground {#000000} \
        -text {Username :} 
    vTcl:DefineAlias "$site_3_0.lab40" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab41 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#c4632b} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font11,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Password :} 
    vTcl:DefineAlias "$site_3_0.lab41" "Label2_1" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent42 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -insertbackground black 
    vTcl:DefineAlias "$site_3_0.ent42" "CustomerLogin_Username" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent43 \
        -background white -disabledforeground {#a3a3a3} -font TkFixedFont \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -insertbackground black \
        -selectbackground {#c4c4c4} -selectforeground black -show * 
    vTcl:DefineAlias "$site_3_0.ent43" "CustomerLogin_Password" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but44 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command Customer_Login \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font11,object) \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Login 
    vTcl:DefineAlias "$site_3_0.but44" "Button1" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but45 \
        -activebackground {#d9d9d9} -activeforeground {#000000} \
        -background {#d9d9d9} -command Customer_Registration \
        -disabledforeground {#a3a3a3} -font $::vTcl(fonts,vTcl:font11,object) \
        -foreground {#000000} -highlightbackground {#d9d9d9} \
        -highlightcolor black -pady 0 -text Registration 
    vTcl:DefineAlias "$site_3_0.but45" "Button1_3" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab39 \
        -in $site_3_0 -x 100 -y 40 -width 262 -relwidth 0 -height 36 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab40 \
        -in $site_3_0 -x 20 -y 120 -width 162 -relwidth 0 -height 26 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab41 \
        -in $site_3_0 -x 10 -y 170 -width 162 -height 26 -anchor nw \
        -bordermode inside 
    place $site_3_0.ent42 \
        -in $site_3_0 -x 170 -y 120 -width 224 -relwidth 0 -height 34 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent43 \
        -in $site_3_0 -x 160 -y 170 -width 224 -height 34 -anchor nw \
        -bordermode inside 
    place $site_3_0.but44 \
        -in $site_3_0 -x 320 -y 230 -width 76 -relwidth 0 -height 33 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but45 \
        -in $site_3_0 -x 150 -y 290 -width 136 -relwidth 0 -height 33 \
        -relheight 0 -anchor nw -bordermode inside 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra38 \
        -in $top -x 10 -y 10 -width 445 -relwidth 0 -height 365 -relheight 0 \
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

